const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");


function authenticate(user, pass)
{
    var success = false;
    $.ajax({
        type: "POST",
        url: '/attempt_create', 
        data: {
            username: user,
            password: pass,
        },
    success: function(data) {
        console.log(data);
        success = true;
        alert("SUCCESS");
    },
    });
    return success;
}

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (authenticate(username,password) === true){
        $.ajax({
            type: "GET",
            url: '/game',
        });
    }
    else {
        loginErrorMsg.style.opacity = 1;
    }
});