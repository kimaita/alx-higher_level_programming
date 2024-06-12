$(function () {
  $('INPUT#btn_translate').on('click', getTranslation);
  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      getTranslation();
    }
  });
});

function getTranslation () {
  const hello = $('DIV#hello');
  const endpoint = 'https://hellosalut.stefanbohacek.dev/';
  const data = { lang: $('INPUT#language_code').val() };

  $.getJSON(endpoint, data, function (resp) {
    hello.text(resp.hello);
  });
}
