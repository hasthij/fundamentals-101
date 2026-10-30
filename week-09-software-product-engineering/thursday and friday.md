Flask Notes

HTTP METHODS
GET - Read something
POST - Send data
PUT - Replace something
PATCH - Change part of something
DELETE - Remove something

STATUS CODES
200 - OK - It worked - Every normal page
302 - Redirect - Go to another address - After saving a form
400 - Bad Request - The request was incomplete - A form field is missing
403 - Forbidden - You are not allowed - Opening someone else’s record
404 - Not Found - No such address - A mistyped URL
405 - Method Not Allowed - Wrong method for this address - POST to a GET-only route
500 - Server Error - Your code crashed - A bug in app.py

CREATING AND ACTIVATING AN ENV
Run in the terminal at the project root:

Create a virtual environment named .venv
python -m venv .venv

Activate it (Windows)
.venv\Scripts\activate


BASIC APP CODE

Import the Flask class
from flask import Flask

Create the app object
app = Flask(name)

Map the URL “/” to the function below
@app.route(“/”)
def home():
return “Hello, world”

TO RUN AN APP
--debug enables auto-reload and the error page

flask --app <main python file name> run --debug

SERVING ROUTES
Static route: fixed URL

@app.route(“/about”)
def about():
return “About this site”

Dynamic route: <name> is captured from the URL and passed to the function

@app.route(“/hello/<name>“)
def hello(name):
return f”Hello, {name}”

COMMON PRACTICE FOR SERVING HTML FILE

main.py
templates
|--->html files
static
|--->style.css

render_template is used to load HTML files with values:

return render_template(“index.html”, title="Home", name="Hasthi")

For the questions asked about the extra name and title: it is to pass data into the HTML site instead of hardcoding values.
The braces you put are not seen by the browser, as when Flask serves it, they are replaced.

{{ ... }} --> Expression --> Prints a value into the page, {{ name }}
{% ... %} --> Statement --> Runs logic such as a loop or an if, prints nothing itself, {% for x in items %}
{# ... #} --> Comment --> Ignored. Never sent to the browser, {# note to self #}

URL_FOR
url_for generates absolute URLs dynamically by looking up Flask route function names or static files, preventing broken links when paths change or nested routes shift.

TEMPLATE INHERITANCE
Use {% extends “base.html” %} to avoid breaking DRY (DON’T REPEAT YOURSELF).

{# Reuse the layout defined in base.html #}
{% extends “base.html” %}

{# Fill the “title” block defined in base.html #}
{% block title %}About Page{% endblock %}

EXAMPLE CODE FOR GETTING DATA FROM A USER

<!-- 1. HTML form: sends the input to /add using POST --> 
<form action="/add" method="post"> 
<!-- name="item" is the key used by request.form["item"] --> 
<input name="item" required> 
<button type="submit">Add</button> </form>

2. Flask Route (Handle POST, extract data, and redirect)
methods=[“POST”] allows this route to receive form submissions

@app.route(“/add”, methods=[“POST”])
def add():
# Read the value typed into the form field named “item”
item_name = request.form[“item”]
# Store it in the list
items.append(item_name)
# Redirect back to the home page (prevents resubmission on refresh)
return redirect(url_for(“home”))

Use urlfor() for linking stylesheets or any static file, to handle dynamic path to file