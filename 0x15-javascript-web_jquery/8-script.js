$(function () {
  const endpoint = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.ajax({
    type: 'GET',
    datatype: 'jsonp',
    url: endpoint,
    success: function (data) {
      $.each(data.results, function (i, film) {
        $('UL#list_movies').append($('<li></li>').text(film.title));
      });
    }
  });
});
