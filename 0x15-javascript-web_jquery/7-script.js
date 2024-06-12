const endpoint = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.getJSON(endpoint, function (actor) {
  $('DIV#character').text(actor.name);
});
