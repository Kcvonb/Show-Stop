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

show = crud.create_show(venue='DNA', show_date=None, show_name='name', location='location', ticket_price=20, num_tickets=200)
model.db.session.add(show)
model.db.session.commit()

ticket = crud.create_ticket_with_id(user.user_id, show.show_id, 20)
model.db.session.add(ticket)
model.db.session.commit()


