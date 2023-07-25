"""Lucky Nums application."""

from models import db, connect_db, LuckyNum
from flask import Flask, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import random, requests

BASE_URL = 'http://numbersapi.com'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234567@localhost:5433/lucky_nums'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
with app.app_context():
    connect_db(app)
    db.create_all()



@app.route("/")
def homepage():
    """Show homepage."""

    return render_template("index.html")


def get_lucky_num():
    """Get a random number between 1 and 100, inclusive."""
    lucky_num = random.randint(1,100)
    return lucky_num


def validate(request):
    """The year entered must be bewteen 1900 and 2000, inclusive, and the
    that color must be one of 'red', 'green', 'orange', 'blue """
    error_data = {"errors": {}}
    required= "This field is required."

    if request["year"] not in range(1900, 2001):
        error_data["errors"]["year"] = "Year must be between 1900 and 2000."

    if request["color"] not in ["red", "green", "orange", "blue"]:
        error_data["errors"]["color"] = "Color is not valid.  Valid colors include red, green, orange, and blue."
    
    for key, val in request.items():
        if val == "":
            error_data["errors"][key] = required
    
    if error_data["errors"] == {}:
        validated = True
        return validated
    else:
        return error_data


def get_data(request):
    user_data = {request}
    response = request.json.get()
    error_data = validate(request)

    if error_data:
        response = {
                "validated": False,
                "error_data": error_data
        }
        json_response = jsonify(response)
        return json_response
    else:
        json_api_data = jsonify(get_api_data(user_data))
        return json_api_data


def get_api_data(lucky_number, year):
    """Get facts for the lucky num and year from the api."""
    lucky_number = get_lucky_num()
    user_data = get_data(request)
    year = user_data["year"]
    
    try:
        num_fact = requests.get(f"BASE_URL/{lucky_number}").text
        year_fact = requests.get(f"BASE_URL/{year}/year").text

        api_data = {
                "num": 
                {
                    "fact": num_fact,
                    "num": lucky_number
                },
                "year":
                {
                    "fact": year_fact,
                    "year": year
                }
            }
        return api_data
    except: 
        api_error = {"message": "please try again...."}
        return api_error
        
    

@app.route("/api/get_lucky_num", methods=["POST"])
def lucky_Num():
    """POST the route to process the form and get json response."""


    data = request.json

    request = LuckyNum(
        name=data['name'],
        birthYear=data['year'],
        email=data['email'],
        color=data['color'])

    validated = validate(request)

    if validated:
        lucky_Num = get_lucky_num()
        lucky_result = get_api_data(lucky_Num, 'year')
    
    return lucky_result



