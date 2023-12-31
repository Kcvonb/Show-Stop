from model import db, Show, Saved, User, Search, connect_to_db

# napalm_death = Show(venue='DNA Lounge', show_name = 'death tour', location = 'address', ticket_price = 20, num_tickets = 200)

def create_show(venue, show_date, show_name, show_id, url):
    show = Show.query.get(show_id)
    if show is None:
        show = Show(venue=venue, show_date=show_date, show_name=show_name, show_id=show_id, url=url)

    return show

def create_saved_with_id(user_id, show_id):

    saved = Saved(user_id=user_id, show_id=show_id)

    return saved

def create_user(email, password, name, user_name):

    user = User(email=email, password=password, name=name, username=user_name)

    return user

def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

def create_search(genre, start_date, end_date, user_id):

    search = Search(genre=genre, start_date=start_date, end_date=end_date, user_id=user_id)

    return search

def get_user_by_id(user_id):
    
    return User.query.filter(User.user_id == user_id).first()

# def get_all_shows










if __name__ =='__main__':
    from server import app
    connect_to_db(app)
     