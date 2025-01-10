#!/usr/bin/python3
"""
================================================================================
FILE NAME: app.py


DESCRIPTION:
------------
This file implements the **Holidays Viewer** application, a Flask-based web app 
that interacts with the MediaWiki Action API to retrieve, display, and manage 
holiday data from Wikipedia. It allows users to view holidays for a given date, 
search for holidays on specific dates, and add new holidays to a test Wikipedia 
page after authentication.

PURPOSE:
--------
1. Fetch and display holidays and observances for:
   - Today's date (default).
   - User-specified dates through a search interface.
2. Enable authenticated users to add new holidays to a test Wikipedia page.
3. Provide a user-friendly and responsive web interface for interacting with 
   holiday data.

USAGE:
------
1. Clone the repository and navigate to the project directory.
2. Install required dependencies using:
   `pip install flask requests`
3. Run the application:
   `python app.py`
4. Access the application in your web browser at: `http://127.0.0.1:5000/`.

KEY COMPONENTS:
---------------
1. **Flask Application**:
   - Routes to handle fetching, displaying, searching, logging in, and adding holidays.
   - Integrated session management for API requests and authentication.

2. **Utility Functions**:
   - `get_todays_date`: Determines the current date for fetching default holiday data.
   - `get_holidays_section`: Identifies the section of Wikipedia pages containing holiday data.
   - `get_holidays`: Retrieves holiday content from Wikipedia sections as HTML.

3. **MediaWiki API Integration**:
   - `action=parse`: Fetches sections and holiday content from Wikipedia.
   - `action=clientlogin`: Authenticates users for editing privileges.
   - `action=edit`: Adds new holidays to a test page on Wikipedia.

4. **Frontend Templates**:
   - HTML templates using Jinja2 for rendering pages:
     - `index.html`: Displays holidays.
     - `search.html`: Search form for specific dates.
     - `login.html`: User authentication interface.
     - `add.html`: Form for adding new holidays.

5. **Styling and Interactivity**:
   - Bootstrap for responsive design and layout.
   - jQuery for updating holiday links dynamically.

IMPLEMENTATION DETAILS:
-----------------------
1. **Flask App Initialization**:
   - The Flask application is initialized with a secret key for managing sessions securely.
   - Routes define the core functionality, including:
     - Listing holidays (`/` or `/<holidays_date>`).
     - Searching for holidays (`/search`).
     - Logging in (`/login`).
     - Adding new holidays (`/add`).

2. **MediaWiki API Integration**:
   - All holiday data is retrieved or modified through the MediaWiki Action API.
   - Sessions ensure API requests are efficient and maintain user authentication.

3. **HTML Templates**:
   - Jinja2 templates dynamically render holiday data and provide user interfaces for searching and adding holidays.

4. **Error Handling and Feedback**:
   - Flash messages inform users about successes (e.g., "Login success!") or errors (e.g., "Oops! Something went wrong.").

5. **Security Considerations**:
   - The application uses a session object for API calls, ensuring minimal data exposure.
   - The secret key should be kept confidential and securely generated.

NOTES:
------
1. The app is intended as a demo and currently supports limited security measures.
2. The test Wikipedia page used for adding holidays is:
   `https://test.wikipedia.org/wiki/Sandbox/Holidays_and_observances`.
3. Ensure network access to both `https://en.wikipedia.org` and `https://test.wikipedia.org` 
   to allow API interactions.
4. While the application supports authentication, advanced user management or role-based 
   permissions are not implemented.

KEY POINTS, IDEAS, AND CONCEPTS:
-------------------------------
1. **Dynamic Date Handling**:
   - Automatically determines today’s date for holiday data or allows user-specified dates.

2. **Modular Utility Functions**:
   - Functions like `get_holidays_section` and `get_holidays` simplify interactions with 
     Wikipedia's API, making the app extensible for future features.

3. **Separation of Concerns**:
   - Flask routes handle application logic, while Jinja2 templates manage presentation 
     for maintainable and scalable code.

4. **API-Driven Design**:
   - The app interacts solely with the MediaWiki Action API, making it adaptable to 
     other MediaWiki instances or extensions.

5. **Scalability**:
   - The modular design and use of sessions enable future enhancements, such as user 
     accounts, more extensive data processing, or integration with additional APIs.

KEY TECHNICAL CODE COMPONENTS:
------------------------------
1. **Route for Listing Holidays**:
   - Displays holidays for the current or a user-selected date, merging test and 
     official holiday data.

2. **Search Route**:
   - Allows users to specify a date and fetch corresponding holiday data.

3. **Login Route**:
   - Authenticates users using the `clientlogin` API endpoint, enabling write privileges 
     for adding new holidays.

4. **Add Route**:
   - Accepts user input for new holidays and posts them to the test Wikipedia page 
     using the `edit` API endpoint.

5. **Utility Functions**:
   - Simplify API interactions, such as retrieving holiday sections, fetching holiday 
     content, and formatting new holiday entries for Wikipedia.

================================================================================
"""


from datetime import datetime
from flask import Flask, render_template, flash, request, url_for, redirect
import requests


APP = Flask(__name__)
APP.secret_key = 'your_secret_key'

URL = "https://en.wikipedia.org/w/api.php"
TEST_URL = "https://test.wikipedia.org/w/api.php"
TEST_PAGE = "Sandbox/Holidays_and_observances"
S = requests.Session()
IS_LOGGED_IN = False

@APP.route('/', methods=['GET', 'POST'])
@APP.route('/<holidays_date>', methods=['GET', 'POST'])
def list_holidays(holidays_date=None):
    """ Lists holidays for the current date or a custom date
    """

    if holidays_date is None:
        holidays_date = get_todays_date()

    # Update date to a custom date
    if request.method == 'POST' and 'search' in request.form:
        search_month = str(request.form.get('monthList'))
        search_day = str(request.form.get('dayList'))
        holidays_date = search_month +"_"+search_day

    # Get the section numbers for the holidays on Wikipedia and for those on the test page
    section_number = get_holidays_section(URL, holidays_date, None)
    test_section_number = get_holidays_section(TEST_URL, TEST_PAGE, holidays_date)

    holidays = get_holidays(URL, holidays_date, section_number)
    test_holidays = get_holidays(TEST_URL, TEST_PAGE, test_section_number)

    holidays_html = test_holidays + holidays
    flash('Holidays added through this app are in bold')

    return render_template("index.html", header=holidays_date.replace('_', ' '),
                           holidays_html=holidays_html)


def get_todays_date():
    """ Get the current month as text and the current day as a number
    """

    current_month = datetime.now().strftime('%B')
    current_day = datetime.now().strftime('%d')
    if current_day.startswith('0'):
        current_day = current_day.replace('0', '')

    return current_month + "_" + current_day

def get_holidays_section(url, page, date_to_get):
    """ Get the section number for holidays on Wikipedia and holidays on the test page
    """

    params = {
        "format":"json",
        "action":"parse",
        "prop":"sections",
        "page":page
    }

    response = S.get(url=url, params=params)
    data = response.json()
    sections = data['parse']['sections']
    section_number = "0"

    for index, value in enumerate(sections):
        if value['anchor'] == "Holidays_and_observances":
            section_number = index + 1

        if url == TEST_URL:
            if value['anchor'] == date_to_get:
                section_number = index + 1

    return section_number

def get_holidays(url, page, section_number):
    """ Get the html which contains holidays
    """

    params = {
        "format":"json",
        "action":"parse",
        "prop":"text",
        "page": page,
        "section": section_number,
        "disableeditsection":1
    }

    response = S.get(url=url, params=params)
    data = response.json()
    text = data['parse']['text']['*']

    return text

@APP.route("/search")
def search():
    """ Search for holidays of custom dates
    """

    return render_template("search.html", header="Search date")

@APP.route("/login", methods=['GET', 'POST'])
def login():
    """ Login to Wikipedia
    """

    if request.method == 'POST' and 'login' in request.form:
        params_0 = {
            "action": "query",
            "meta": "tokens",
            "type": "login",
            "format": "json"
        }

        response = S.get(url=URL, params=params_0)
        data = response.json()

        login_token = data['query']['tokens']['logintoken']

        params_1 = {
            "action": "clientlogin",
            "username": str(request.form.get('username')),
            "password": str(request.form.get('password')),
            "loginreturnurl": "http://127.0.0.1:5000/login",
            "logintoken": login_token,
            "format": "json"
        }

        response = S.post(url=URL, data=params_1)
        data = response.json()

        if data['clientlogin']['status'] != 'PASS':
            flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])
        else:
            global IS_LOGGED_IN
            IS_LOGGED_IN = True
            flash('Login success! Welcome, ' + data['clientlogin']['username'] + '!')
            return redirect(url_for('add'))

    return render_template("login.html", header="Login")

@APP.route("/add", methods=['GET', 'POST'])
def add():
    """ Add a new holiday to a test page and redirect to that date's holidays to show the added holidays
    """

    if not IS_LOGGED_IN:
        return redirect(url_for('login'))

    if request.method == 'POST' and 'add' in request.form:

        # Wiki markup to format the added holiday's text as a list item and in bold
        holiday_text = "* '''" + str(request.form.get('description')) + "'''"
        date = str(request.form.get('date'))

        params_2 = {
            "action": "query",
            "meta": "tokens",
            "format": "json"
        }

        response = S.get(url=TEST_URL, params=params_2)
        data = response.json()

        csrf_token = data['query']['tokens']['csrftoken']

        params_4 = {
            "action": "edit",
            "title": TEST_PAGE,
            "token": csrf_token,
            "format": "json",
            "section": "new",
            "sectiontitle": date,
            "text": holiday_text,
        }

        response = S.post(url=TEST_URL, data=params_4)
        data = response.json()

        if data['edit']['result'] != 'Success':
            flash('Oops! Something went wrong -- ' + data['clientlogin']['messagecode'])
        else:
            flash('New holiday added successfully!')
            return redirect(url_for('list_holidays', holidays_date=date.replace(' ', '_')))

    return render_template("add.html", header="Add holiday")

app = APP  # Expose APP as app for Vercel compatibility

if __name__ == "__main__":
    APP.run()
