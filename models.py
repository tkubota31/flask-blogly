"""Models for Blogly."""
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

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
