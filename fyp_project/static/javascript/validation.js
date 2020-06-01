//Signin verification

function verify_sign_in() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
}

//Account details for registration

function get_sign_up() {
    var first_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
}

//Signup validation

function validate_sign_up() {
    var password_1 = document.getElementById("password").value;
    var password_2 = document.getElementById("confirm_password").value;
    if (password_2 != password_1) {
        alert("Passwords do not match.");
        return false;
    }
}

//Password change validation

function validate_password() {
    var new_password = document.getElementById("new_password").value;
    var confirm_password = document.getElementById("confirm_new_password").value;
    if (confirm_password != new_password) {
        alert("Passwords do not match.");
        return false;
    }
}

//Name change validation

function validate_name() {
    var first_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    return true;
}