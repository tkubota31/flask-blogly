"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy
DEBUG_TB_INTERCEPT_REDIRECTS = False
db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

#MODELS GO HERE

class User(db.Model):
    __tablename__ = "User"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)

    first_name = db.Column(db.Text,
                        nullable = False)
    last_name = db.Column(db.Text,
                        nullable = False)
    image_url = db.Column(db.Text, nullable = False)

    posts = db.relationship("Post", backref="user")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "Post"

    id = db.Column(db.Integer,
                    primary_key =True,
                    autoincrement = True)

    title = db.Column(db.Text,
                        nullable = False)
    content = db.Column(db.Text,
                        nullable=False)
    create_at = db.Column(db.DateTime,
                            nullable=False,
                             default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
