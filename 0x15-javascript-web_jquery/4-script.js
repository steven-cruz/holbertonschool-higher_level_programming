/*
  Javascript that toggles the class of the HTML tag HEADER to red (#FF0000)
  when the user clicks on the tag DIV#toggle_header:
  - The HEADER tag must always have one class: red or green,
    never both in the same time, never empty.
*/
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
