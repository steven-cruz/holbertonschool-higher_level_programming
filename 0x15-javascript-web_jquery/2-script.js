/*
  JavaScript that updates the tect color of the HTML tag HEADER to red
  (#FF0000) when the user clicks on the tag DIV#red_herader
*/
$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});
