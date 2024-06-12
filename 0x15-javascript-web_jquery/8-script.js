const endpoint = 'https://swapi-api.alx-tools.com/api/films/?format=json';
const list = $('UL#list_movies');

$.getJSON(endpoint, function (films) {
  $.each(films.results, function (i, film) {
    const item = $('<li></li>').text(film.title);
    list.append(item);
  });
});
