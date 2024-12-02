function addRandomGenre() {
    fetch('/add_random_genre')
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        alert(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function addRandomActor() {
    fetch('/add_random_actor')
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        alert(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function addRandomDirector() {
    fetch('/add_random_director')
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        alert(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
function generateMovies() {
    // Functionality to generate movies
    var numberOfMovies = document.getElementById('numberOfMovies').value;
    alert('Generating ' + numberOfMovies + ' movies');
}

function searchByYear() {
    // Functionality to search movies by year
    var year = document.getElementById('searchByYear').value;
    alert('Searching movies released in ' + year);
}

function searchByYearRange() {
    // Functionality to search movies by year range
    var startYear = document.getElementById('startYear').value;
    var endYear = document.getElementById('endYear').value;
    alert('Searching movies released between ' + startYear + ' and ' + endYear);
}

function generateMovies(){
    const num_movies = document.getElementById('num_movies').value;

    if (!num_movies || isNaN(num_movies) || num_movies <= 0) {
        alert("Please enter a valid number of movies.");
        return;
    }

    fetch(`/generate_movie_title/${num_movies}`)
    .then(response => {
        if (response.ok) {
            return response.text();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        alert('Successfully Generated and added ' + num_movies + ' movies');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}