from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

# Predefined lists of genres, actors, and directors
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]
actors = ["Tom Hanks", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Angelina Jolie"]
directors = ["Steven Spielberg", "Christopher Nolan", "Quentin Tarantino", "Martin Scorsese", "James Cameron"]

# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('movies_database.db')
    return conn

# Route to generate and store random genre
@app.route('/add_random_genre')
def add_random_genre():
    genre = random.choice(genres)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO genres (genre_name) VALUES (?)", (genre,))
    conn.commit()
    conn.close()
    return "Random genre added: {}".format(genre)

# Route to generate and store random actor
@app.route('/add_random_actor')
def add_random_actor():
    actor = random.choice(actors)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO actors (actor_name) VALUES (?)", (actor,))
    conn.commit()
    conn.close()
    return "Random actor added: {}".format(actor)

# Route to generate and store random director
@app.route('/add_random_director')
def add_random_director():
    director = random.choice(directors)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO directors (director_name) VALUES (?)", (director,))
    conn.commit()
    conn.close()
    return "Random director added: {}".format(director)

# Initialize the database schema
def init_db():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS genres
                      (genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      genre_name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS actors
                      (actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      actor_name TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS directors
                      (director_id INTEGER PRIMARY KEY AUTOINCREMENT,
                      director_name TEXT,
                      birth_date TEXT)''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
