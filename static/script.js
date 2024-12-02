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

function searchByYear(){
    const year = document.getElementById('searchByYear').value;

    if (!year || isNaN(year) || year <= 0) {
        alert("Please enter a valid year.");
        return;
    }

    fetch(`/search_movies_by_year?year=${year}`)
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data);
        //alert(`Found ${data.count} movies released in ${year}`);
        document.getElementById('searchByYearExecuteTime').innerHTML = `Execution time: ${data.time} seconds`;
        document.getElementById('searchByYearNumMoviesFound').innerHTML = `Found ${data.count} movies released in ${year}`;

    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while searching for movies.");
    });

}

function searchByYearRange (){
    const startYear = document.getElementById('startYear').value;
    const endYear = document.getElementById('endYear').value;

    if (!startYear || isNaN(startYear) || startYear <= 0 || !endYear || isNaN(endYear) || endYear <= 0 ) {
        alert("Please enter a valid year range.");
        return;
    }
    
    if (startYear > endYear){
        alert("Start year cannot be bigger than end year.");
        return;
    }
    fetch(`/search_movies_by_year_range?startYear=${startYear}&endYear=${endYear}`)
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log(data);
        //fill the document id searchByYearExecuteTime and searchByYearNumMoviesFound
        document.getElementById('searchByYearRangeExecuteTime').innerHTML = `Execution time: ${data.time} seconds`;
        document.getElementById('searchByRangeYearNumMoviesFound').innerHTML = `Found ${data.count} movies released in between ${startYear} and ${endYear}`;

    })
    .catch(error => {
        console.error('Error:', error);
        alert("An error occurred while searching for movies.");
    });
}