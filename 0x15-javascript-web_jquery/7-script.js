$(function () {
  const endpoint = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.ajax({
    type: 'GET',
    datatype: 'jsonp',
    url: endpoint,
    success: function (data) {
      $('DIV#character').text(data.name);
    }
  });
});
