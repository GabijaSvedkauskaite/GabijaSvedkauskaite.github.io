from flask_login import UserMixin
from peewee import *

database = SqliteDatabase('movies.db')

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel, UserMixin):
    username = CharField(unique=True)
    password = CharField()
    
    @classmethod
    def authenticate(cls, username, password):
        try:
            return cls.get(cls.username == username and cls.password == password)
        except cls.DoesNotExist:
            return None

class Movie(BaseModel):
    user = ForeignKeyField(User, backref='movies')
    movie_id = IntegerField()

def initialize_database():
    database.connect()
    database.create_tables([User, Movie], safe=True)
    database.close()

def create_user(username, password):
    user = User(username=username, password=password)
    user.save()

