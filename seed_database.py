import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb show-stop')
os.system('createdb show-stop')

model.connect_to_db(server.app)
model.db.create_all()

# with open("data/shows.json") as f:
#     show_data = json.loads(f.read())

user = crud.create_user('email','password')
model.db.session.add(user)
model.db.session.commit()

show = crud.create_show(venue='venue', show_date=None, show_name='show_name', location='location', ticket_price=ticket_price, num_tickets=num_tickets)
model.db.session.add(show)
model.db.session.commit()

ticket = crud.create_ticket_with_id(user.user_id, show.show_id, 20)
model.db.session.add(ticket)
model.db.session.commit()

search = crud.create_search(genre=genre, start_date=start_date, end_date=end_date, user_id=user_id)
model.db.session.add(search)
model.db.session.commit()

