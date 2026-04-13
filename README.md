# Summarize Notes

## Description

Summarize Notes is a web application designed to help users quickly extract the most importance information from a collection of notes. After accepting raw notes as input, this web application processes them using a prompt to the AI model, and returns a concise summary of up to three key points. Each summary is stores in a local SQL database alongside the meeting title, allowing users to retreive past summaries. This web application was built using Flask in Python, leverages OpenAI's GPT-3.5 Turbo generative AI language model, and stores summaries in an SQL database.

This web application was developed as the final assignment for MGMT4620: Web Design and Architecture and serves as an example of how social problems can now be solved using generative AI.

## Usage

### Setup

**NOTE:** Usage may differ depending on the version of Python installed and prefered running method. This guide uses Python 3 and commands are run in the MacOS command line interface (CLI).

**1. Clone or download the project files from https://github.com/averysully/Summarize-Notes.**

**2. Ensure your environment is configured with the required libraries.**
```
pip3 install flask openai python-dotenv
```

**3. Add your OpenAI API key to `.env`**
```
OPENAI_API_KEY=""
```

**4. Run `init_db.py` to initialize the database by entering the following command in the CLI.**
```
python3 init_db.py
```

**5. Run the web app by entering the following command in the CLI.**
```
flask run
```

**6. Enter the following into your browser to open the web app.**
```
http://127.0.0.1:5000
```

### Summarizing Notes

Once the web app is running in your browser at `http://127.0.0.1:5000`, notes can be summarized by entering them into **Meeting Notes**. Each meeting must also be given title by entering one into **Meeting Title**. Once complete, clicking the `Submit` button will initiate a connection to OpenAI's GPT-3.5 Turbo to summarize the notes. The response is then logged in the SQL database and displayed below the entry boxes.

### Searching Summaries

Scrolling down on the web app will reveal a secondary feature to search the database using the given title. Entering the desired title into **Search Past Summaries** and clicking the `Search` button will query the database for possible result. If one exists, it will be displayed below the entry box.

## Structure

```
Summarize-Notes/
    app.py
    init_db.py
    schema.sql
    database.db
    .env
    templates/
        index.html
    static/
        main.css
```

## Acknowledgements

This project was structured using existing code, rebtrainer by Colin Conrad, provided during the winter 2026 offering of MGMT4620: Web Design and Architecture for Case Assignment 2. Personal additions and modifications made in this project extended on the fundamentals demonstrated during this assignment, such as application structure, database writing and searching, and the HTML/CSS styling.