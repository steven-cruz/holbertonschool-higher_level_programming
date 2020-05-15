/*
  JavaScript that updates the tect color of the HTML tag HEADER to red
  (#FF0000) when the user clicks on the tag DIV#red_herader
*/
$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
