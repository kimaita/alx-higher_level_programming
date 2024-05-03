$(function () {
  const endpoint = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').on('click', function () {
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
  });
});
