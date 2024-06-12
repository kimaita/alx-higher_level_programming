$(function () {
  const list = $('UL.my_list');
  $('DIV#add_item').on('click', function () {
    const item = $('<li>Item</li>');
    list.append(item);
  });
  $('DIV#remove_item').on('click', function () {
    $('li').eq(-1).remove();
  });
  $('DIV#clear_list').on('click', function () {
    list.empty();
  });
});
