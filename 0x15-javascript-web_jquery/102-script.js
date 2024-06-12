$(function () {
  const hello = $('DIV#hello');
  const endpoint = 'https://hellosalut.stefanbohacek.dev/';

  $('INPUT#btn_translate').on('click', function () {
    const data = { lang: $('INPUT#language_code').val() };
    $.getJSON(endpoint, data, function (resp) {
      hello.text(resp.hello);
    });
  });
});
