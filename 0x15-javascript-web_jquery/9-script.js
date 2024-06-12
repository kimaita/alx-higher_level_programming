const endpoint = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$.getJSON(endpoint, function (resp) {
  console.log(resp.hello);
  $('DIV#hello').text(resp.hello);
});
