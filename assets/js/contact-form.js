var submitted=false;

$('#gform').on('submit',function(e){
  $('#gform *').fadeOut(500);
  $('#gform').prepend('<h3>Your submission is received, we will contact you shortly !</h3><br><br>For order related queries email support@haveeka.com');
  });