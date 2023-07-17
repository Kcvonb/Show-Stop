from model import db, Show, Ticket, User, connect_to_db

# napalm_death = Show(venue='DNA Lounge', show_name = 'death tour', location = 'address', ticket_price = 20, num_tickets = 200)

def create_show(venue, show_date, show_name, location, ticket_price, num_tickets):

    show = Show(venue=venue, show_date=show_date, show_name=show_name, location=location, ticket_price=ticket_price, num_tickets=num_tickets)

    return show

def create_ticket_with_id(user_id, show_id,ticket_price):

    ticket = Ticket(user_id=user_id, show_id=show_id, ticket_price=ticket_price)

    return ticket

def create_user(email, password):

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):
    
    return User.query.filter(User.email == email).first()

# def get_all_shows










if __name__ =='__main__':
    from server import app
    connect_to_db(app)
     