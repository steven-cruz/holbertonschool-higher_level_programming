/*
  Write a Javascript script that adds a LI element to a list when the user
  clicks on the tag DIV#add_item
*/
$('#add_item').click(function (){
  const $ul = $('UL.my_list');
  $ul.append('<li>Item</li>');
});
