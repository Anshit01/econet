function validate() {
    console.log("run");
  var name = $("#input-username").val();
//   var email = $("#email").val();
  var password = $("#input-password").val();
  var password_confirm = $("#input-confirm-password").val();
  var warning = $("#warning");

  if (
    name == "" ||
    // email == "" ||
    password == "" ||
    password_confirm == ""
  ) {
    warning.html("All fields are required.");
    glowWarning();
    return false;
  }
  if(name.length < 3 ){
    warning.html("Username too short");
    glowWarning();
    return false;
  }
  else if(name.length > 10 ){
    warning.html("Username too long");
    glowWarning();
    return false;
  }
  var regex_name = /^[a-zA-Z0-9_]{3,10}$/;
//   var regex_email = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  var msg = "";
  if (regex_name.test(name) == false) {
    msg = "Invalid name";
  }
//    else if (regex_email.test(email) == false) {
//     msg = "Invalid email ID";
//   }
   else if (password != password_confirm) {
    msg = "Passwords does not match";
  } else {
    return true;
  }
  warning.html(msg);
  glowWarning();
  return false;
}

function glowWarning() {
  var warning = $("#warning");
  warning.css("text-shadow", "0 0 50px red, 0 0 20px red, 0 0 10px red");
  setTimeout(function () {
    warning.css("text-shadow", "none");
  }, 300);
}
