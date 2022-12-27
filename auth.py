from flask_login import login_user, logout_user, current_user
from models import User

def login(username, password):
    user = User.authenticate(username, password)
    if user:
        login_user(user)

def logout():
    logout_user()

def change_password(password):
    current_user.password = password
    current_user.save()
