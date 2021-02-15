var email = document.getElementById("email");
var pwd = document.getElementById("pwd");
var conf = document.getElementById("conf");
var button = document.getElementById("register");

button.onclick = function() {
	if (pwd.value === conf.value) {
		window.alert(email.value + "\n" + pwd.value)
	} else {
		window.alert("Password and confirmation are different")
	}
};
