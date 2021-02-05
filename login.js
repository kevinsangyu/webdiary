var button = document.getElementById("login");
var email = document.getElementById("email");
var pwd = document.getElementById("pwd");

button.onclick = function() {
	window.alert(email.value + "\n" +  pwd.value)
};
