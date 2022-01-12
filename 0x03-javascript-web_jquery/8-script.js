$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (let i = 0; i < data.results.length; ++i) {
    console.log(data.results[i]);
    $('#list_movies').append('<li>' + data.results[i].title + '</li>')
  }
});
