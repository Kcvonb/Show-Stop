from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
import os
import requests
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    """View homepage."""

    return render_template("homepage.html")

@app.route('/registration')
def create_acct():

    return render_template("create_acct.html")

@app.route("/users", methods=["POST"])
def register_user():
    """Create a new user."""
    
    email = request.form.get("email")
    password = request.form.get("password")
    print(email, password)
    user = crud.get_user_by_email(email)
    if user: 
        flash("That email is already in use. Please try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        

    return redirect("/search")

@app.route("/search")
def search():

    return render_template("search_form.html")

@app.route("/search_info", methods=["POST"])
def search_info():

    genre = request.form.get('genre')

    payload={'apikey': os.environ['TICKETMASTER_KEY'], 'city': 'San Francisco', 'keyword': 'music', 'classificationName': genre}
    res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json", params=payload)
    data = res.json()
    events = data['_embedded']['events']
    print(events[0])
    # import pdb;pdb.set_trace()
    return render_template("results.html", event_list=events)

@app.route("/login", methods=['POST'])
def login():

    return redirect('/search') 

def remove_duplicates_from_list(input_list):
    return list(set(input_list))

# @app.route("")







if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)