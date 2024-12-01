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
