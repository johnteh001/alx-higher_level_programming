#!/user/bin/node
$('#add_item').click(function () {
  const item = $('<li></li>').text('Item 1');
  $('.my_list').append(item);
});
