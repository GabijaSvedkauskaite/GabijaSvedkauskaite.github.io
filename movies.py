import requests
from config import API_KEY
import json

# Get the base URL for movie posters
poster_base_url = 'https://image.tmdb.org/t/p/original'

def get_popular_movies():
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}")
    return response.json()

def display_movies(movies):
    # Display the movies in a grid of 3 per row
    for i, movie in enumerate(movies):
        # Construct the full URL to the movie poster image
        poster_url = f'{poster_base_url}{movie["poster_path"]}'
        # Print the movie title and poster URL
        print(f'Title: {movie["title"]}')
        print(f'Poster URL: {poster_url}')
        # If this is the third movie in the row, start a new row
        if (i + 1) % 3 == 0:
            print()

# Test the display_movies() function
movies = get_popular_movies()
display_movies(movies["results"])



def search_movies(query):
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}'
    response = requests.get(url)
    results = response.json()['results']
    return results

def add_movie(user_id, movie_id):
    movie = Movie(user_id=user_id, movie_id=movie_id)
    movie.save()

# Test the get_popular_movies() function
movies = get_popular_movies()
display_movies(movies["results"])

# Test the search_movies() function
results = search_movies("Avengers")
display_movies(results)
