import os
import dotenv
import sqlite3
from flask import Flask, render_template, request
from openai import OpenAI

dotenv.load_dotenv()
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    result = None
    summary = None
    not_found = None

    if request.method == "POST":

        if "notes" in request.form: # note summarizer

            title = request.form["title"]
            notes = request.form["notes"]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=0.5,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Your task is to serve as a meeting summarizer."
                            "The meeting notes provided to you need to be summarized into the 3 most important points."
                            "If there is not 3 notable points, only create as many as you can."
                            "Do not create anything other than the sentences below. This means no introduction, closing statement, etc."
                            "1. 1 sentence describing the first point."
                            "2. 1 sentence describing the second point."
                            "3. 1 sentence describing the third point."
                        )
                    },
                    {
                        "role": "user",
                        "content": notes
                    }
                ]
            )
            result=response.choices[0].message.content

            lines = [line.strip() for line in result.strip().splitlines() if line.strip()]
            point1 = lines[0] if len(lines) > 0 else None
            point2 = lines[1] if len(lines) > 1 else None
            point3 = lines[2] if len(lines) > 2 else None

            conn = get_db_connection()
            conn.execute("INSERT INTO summary (title, point1, point2, point3) VALUES (?, ?, ?, ?)", (title, point1, point2, point3))
            conn.commit()
            conn.close()

        elif "search_title" in request.form: # summary search

            search_title = request.form["search_title"]
            conn = get_db_connection()
            row = conn.execute(
                "SELECT * FROM summary WHERE title = ? ORDER BY Created DESC LIMIT 1",
                (search_title,)
            ).fetchone()
            conn.close()
            if row:
                summary = row
            else:
                not_found = True

    return render_template("index.html", result=result, summary=summary, not_found=not_found)