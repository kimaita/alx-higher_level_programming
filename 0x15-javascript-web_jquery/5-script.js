$('DIV#add_item').on('click', function () {
  $('UL.my_list').append($('<li></li>').text('Item'));
});
