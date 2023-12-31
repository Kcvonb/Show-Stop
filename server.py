from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
import os
import requests
from jinja2 import StrictUndefined
import datetime

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
    name = request.form.get("name")
    user_name = request.form.get("user_name")
    print(email, password)
    user = crud.get_user_by_email(email)
    if user: 
        flash("That email is already in use. Please try again.")
    else:
        user = crud.create_user(email, password, name, user_name)
        db.session.add(user)
        db.session.commit()

        session ['user']=user.user_id
        flash('Login and account creation successful!')
    return redirect('/user')
        

@app.route("/search")
def search():

    return render_template("search_form.html")

@app.route("/search_info", methods=["POST"])
def search_info():

    genre = request.form.get('genre')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    start_date_obj=datetime.datetime.strptime(start_date,'%Y-%m-%d')
    end_date_obj=datetime.datetime.strptime(end_date,'%Y-%m-%d')
 
    iso_range=start_date_obj.isoformat() + 'Z,' + end_date_obj.isoformat() + 'Z'
   
    print(iso_range)

    payload={'apikey': os.environ['TICKETMASTER_KEY'], 'city': 'San Francisco', 'keyword': 'music', 'classificationName': genre, 'startEndDateTime' : iso_range} 
    
    res = requests.get("https://app.ticketmaster.com/discovery/v2/events.json", params=payload)
    data = res.json()
    print(data)

    if '_embedded' in data:
        events = data['_embedded']['events']

    else: 
        events = {}
        flash('No results within your search, please broaden your search.')
   
   
    return render_template("results.html", event_list=events)


@app.route("/login", methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    print(email)
    print(password)
    print (user)
    if user is None:
        flash('User not found')
        return redirect('/')
    if password == user.password:
        #implement user page
        #make sure temp inherit from base
        session ['user']=user.user_id
        flash('Login successful')
    else:
        flash('Password incorrect, try again')
        return redirect('/')
    return redirect('/user') 

@app.route("/user") #goal of app route is to redirect login to userpage
def user():
    user_id = session.get('user')
    if user_id == None:
        return redirect('/')#change email to name
    else:
        user = crud.get_user_by_id(user_id)
        return render_template('user.html', user = user)
    
@app.route('/saved', methods=['POST'])
def saved():
    show_id = request.json.get('show_id')
    name = request.json.get('name')
    date = request.json.get('date')
    url = request.json.get('url')
    print(dir(request))
    # import pdb; pdb.set_trace()
   
    print(show_id, name, date)
    user_id = session.get('user')
    show = crud.create_show(venue=None, show_date=date, show_name=name, show_id=show_id, url=url)
    db.session.add(show)
    saved = crud.create_saved_with_id(user_id=user_id, show_id=show_id)
    db.session.add(saved)
    db.session.commit()
    #relate show to a saved obj created
    #add obj to db.session-commit
    #send back to front end saying whether we were successful in getting done
    #front end dom manipulation 
    return{'message': 'Your show has been successfully saved.', 'status': 200}





def remove_duplicates_from_list(input_list):
    return list(set(input_list))

# @app.route("")







if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)