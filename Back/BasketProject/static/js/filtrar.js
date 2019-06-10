$(document).ready(function(){
  $("#barra").keyup(function(){
    var value = $(this).val().toLowerCase();
    $("#cuerpo tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});
