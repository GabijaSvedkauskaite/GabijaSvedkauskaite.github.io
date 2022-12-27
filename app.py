from flask import Flask, render_template, request, redirect, url_for
from movies import search_movies, add_movie, get_popular_movies, display_movies
from auth import login, logout, change_password
from models import User, Movie
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = '7310064772asdaSD'

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == user_id)

@app.route('/home')
@login_required
def index():
    movies = get_popular_movies()
    return render_template('index.html', movies=movies["results"], current_user=current_user)

@app.route('/myList')
@login_required
def myList():
    return render_template('mylist.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_movies(query)
    return render_template('search.html', results=results)

@app.route('/add', methods=['POST'])
def add():
    movie_id = request.form['movie_id']
    add_movie(current_user.id, movie_id)
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        current_user.password = request.form['password']
        current_user.save()
        return redirect(url_for('index'))
    else:
        return render_template('settings.html')


if __name__ == '__main__':
    initialize_database()
    create_user('username', 'password')
    app.run(debug=True)
