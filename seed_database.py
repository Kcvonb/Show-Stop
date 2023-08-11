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
#     show_data = json.loads(f.read())s

user = crud.create_user('email','password','name','username')
model.db.session.add(user)
model.db.session.commit()

show = crud.create_show(venue='venue', show_id='1', show_date=None, show_name='show_name', ticket_price=7,)
model.db.session.add(show)
model.db.session.commit()

ticket = crud.create_ticket_with_id(user.user_id, show.show_id, 20)
model.db.session.add(ticket)
model.db.session.commit()

test = User(name='test', email='test@test.com', password='test', username='testy')
model.db.session.add(test)
model.db.session.commit()
