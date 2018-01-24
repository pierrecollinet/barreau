$(function() {
  var current_path = location.pathname.split("/")[1]
  if (current_path == "") {
    $('#accueil').addClass('active');
  } else {
    $(`#${current_path}`).addClass('active');
  }
});
