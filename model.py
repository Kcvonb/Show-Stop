from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Show (db.Model):

    __tablename__ = 'shows'

    show_id = db.Column(db.String,
                        primary_key=True)
    venue = db.Column(db.String)
    show_date = db.Column(db.DateTime)
    show_name = db.Column(db.String)
    url = db.Column(db.String)
   
    saves = db.relationship('Saved', back_populates='show')

    def __repr__(self):
        return f'<Show show_name={self.show_name} show_id={self.show_id}>'

class Saved (db.Model):
    __tablename__ = 'saves'
    saved_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    show_id = db.Column(db.String, db.ForeignKey('shows.show_id'), nullable=True)
   

    show = db.relationship("Show", back_populates="saves")
    user = db.relationship("User", back_populates="saves")


    def __repr__(self):
        return f'<Saved saved_id={self.saved_id} show_id={self.show_id} user_id={self.user_id}>'

class User (db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    username = db.Column(db.String)

    saves = db.relationship('Saved', back_populates='user')
    searches = db.relationship('Search', back_populates='user')

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'
    
class Search (db.Model):

    __tablename__ = 'searches'

    search_id = db.Column(db.Integer,
                          primary_key=True)
    genre = db.Column(db.String)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    user = db.relationship('User', back_populates='searches')
                        
    def __repr__(self):
        return f'<Search search_id={self.search_id} genre={self.genre}>'
    




               




def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///show-stop"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")




if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)