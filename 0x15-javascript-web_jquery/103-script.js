function getTranslation () {
  const endpoint = 'https://hellosalut.stefanbohacek.dev/';
  const userLang = $('INPUT#language_code').val();
  $.ajax({
    url: endpoint,
    type: 'GET',
    data: { lang: userLang },
    datatype: 'jsonp',
    success: function (data) {
      $('DIV#hello').text(data.hello);
    }
  });
}

$(function () {
  $('INPUT#btn_translate').on('click', getTranslation);
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      getTranslation();
    }
  });
});
