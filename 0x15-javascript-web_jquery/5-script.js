const list = $('UL.my_list');
const item = $('<li>Item</li>');

$('DIV#add_item').on('click', function () {
  list.append(item);
});
