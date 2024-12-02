from flask import Flask, render_template, request, jsonify
import sqlite3
import random
import time #will be used later to get the time it took to search for movies by year
app = Flask(__name__)

# Predefined lists of genres, actors, and directors
genres = [
    "Action", "Comedy", "Drama", "Horror", "Sci-Fi", 
    "Adventure", "Fantasy", "Thriller", "Romance", "Mystery", 
    "Musical", "Western", "Crime", "Biography", "Historical", 
    "War", "Animation", "Documentary", "Family", "Sports", 
    "Noir", "Epic", "Superhero", "Experimental"]
actors = [
    "Tom Hanks", "Leonardo DiCaprio", "Meryl Streep", "Brad Pitt", "Angelina Jolie",
    "Robert Downey Jr.", "Scarlett Johansson", "Denzel Washington", "Jennifer Lawrence", "Ryan Gosling", 
    "Chris Hemsworth", "Emma Watson", "Zendaya", "Johnny Depp", "Anne Hathaway", 
    "Samuel L. Jackson", "Natalie Portman", "Christian Bale", "Gal Gadot", "Viola Davis", 
    "Keanu Reeves", "Margot Robbie", "Joaquin Phoenix", "Eddie Redmayne", "Florence Pugh"
]
directors = [
    "Steven Spielberg", "Christopher Nolan", "Quentin Tarantino", "Martin Scorsese", "James Cameron", 
    "Denis Villeneuve", "Greta Gerwig", "Bong Joon-ho", "Ridley Scott", "Jordan Peele", 
    "Wes Anderson", "Alfred Hitchcock", "George Lucas", "Francis Ford Coppola", "Sofia Coppola", 
    "Taika Waititi", "Guillermo del Toro", "Patti Jenkins", "Peter Jackson", "Ang Lee", 
    "David Fincher", "Stanley Kubrick", "Spike Lee", "Tim Burton", "Kathryn Bigelow"
]
adjectives = [
    "Amazing", "Bewitched", "Charming", "Dazzling", "Enigmatic",
    "Fantastic", "Glorious", "Harmonious", "Incredible", "Jubilant",
    "Magical", "Radiant", "Spectacular", "Thrilling", "Wonderous",
    "Majestic", "Heroic", "Vivid", "Ethereal", "Graceful",
    "Fearless", "Luminous", "Epic", "Fierce", "Bold",
    "Mysterious", "Serene", "Timeless", "Brilliant", "Vibrant",
    "Elegant", "Mesmerizing", "Dynamic", "Legendary", "Exquisite"
]
nouns = [
    "Adventure", "Dream", "Escape", "Fantasy", "Journey",
    "Mystery", "Odyssey", "Quest", "Voyage", "Legend",
    "Miracle", "Enchantment", "Whisper", "Wonder", "Treasure",
    "Saga", "Chronicle", "Tale", "Eclipse", "Illusion",
    "Promise", "Revelation", "Destiny", "Vision", "Horizon",
    "Shadow", "Echo", "Haven", "Paradox", "Prophecy",
    "Labyrinth", "Myth", "Infinity", "Legacy", "Awakening"
]
descriptions = [
    "An epic tale of adventure.", "A gripping drama about life and love.", 
    "A chilling horror story.", "A heartwarming comedy.", 
    "A futuristic sci-fi masterpiece."
]

def generate_movie_title():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)
    return f"{adjective} {noun} {random_number}"
# Function to connect to the database
def connect_db():
    conn = sqlite3.connect('db/movies_database.db')
    return conn
#route to get to home page
@app.route('/')
def index():
    return render_template('index.html')
#helper function to generate title
def generate_random_title():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)
    return f"{adjective} {noun} {random_number}"

#route to genreate movie title
@app.route('/generate_movie_title/<int:num_movies>')
def generate_movie_title(num_movies):
    conn = connect_db()
    try:
        cursor = conn.cursor()
        for _ in range(num_movies):
            title = generate_random_title() 
            release_year = random.randint(1980, 2024)
            rating = round(random.uniform(1, 10), 1)
            description = random.choice(descriptions)
            cursor.execute(
                'INSERT INTO Movies (title, release_year, rating, description) VALUES (?, ?, ?, ?)',
                (title, release_year, rating, description)
            )
        conn.commit()
        return "Movies generated successfully"
    except Exception as e:
        return f"An error occurred: {e}", 500
    finally:
        conn.close()
        return f"{num_movies} movies generated successfully."

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

#serach movies by year
@app.route('/search_movies_by_year', methods=['GET']) #using query param
def search_movies_by_year():
    start_time = time.time()
    year = request.args.get('year')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM Movies WHERE release_year = ?", (year,))
    count = cursor.fetchone()[0]
    conn.close()
    end_time = time.time()
    return {"count": count, "time": end_time - start_time} 

#search movies by year range
@app.route('/search_movies_by_year_range', methods=['GET']) #using query param
def search_movies_by_year_range():
    start_time = time.time()
    start_year = request.args.get('startYear')
    end_year = request.args.get('endYear')
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) FROM Movies WHERE release_year BETWEEN ? AND ?", (start_year, end_year))
    count = cursor.fetchone()[0]
    conn.close()
    end_time = time.time()
    return {"count": count, "time": end_time - start_time}

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
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_release_year ON Movies(release_year)')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
