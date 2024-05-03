$(function () {
  const endpoint = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  $.ajax({
    type: 'GET',
    datatype: 'jsonp',
    url: endpoint,
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
});
