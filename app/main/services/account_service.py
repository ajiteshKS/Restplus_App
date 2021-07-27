import uuid

from flask import session, g
from app import init_db
from app.main.models.user import db, User
from datetime import datetime as dt


def add_new_user(username, password, email, bio):
    """Create a user in MySQL db"""
    new_user = User(username=username,
                    password=password,
                    email=email,
                    created=dt.now(),
                    bio=bio,
                    admin=False)  # Create an instance of the User class
    db.session.add(new_user)  # Adds new User record to Model
    db.session.commit()


def authenticate_user(username, password):
    error = None
    row_fetched = User.query.filter(User.username == username)
    user = row_fetched.first()
    if row_fetched.count() > 0 and username == user.username:
        if password != user.password:
            error = 'Incorrect password'
    else:
        error = 'No such user'
    return error


def add_in_redis(username):
    g.db = init_db()
    session_id = int(uuid.uuid4())
    session['username'] = username
    session['session_id'] = session_id
    g.db.hsetnx('user', session_id, username)

def remove_from_redis(session_id):
    g.db = init_db()
    g.db.hdel('user', session_id)
    session.pop('username', None)
    session.pop('session_id', None)
