const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");


function authenticate(user, pass)
{
    return new Promise(
    $.ajax({
        type: "POST",
        url: '/attempt_create', 
        data: {
            username: user,
            password: pass,
        },
    success: function(data) {
        loginButton.setAttribute('status', data)
    },
    }));
    
}


loginButton.addEventListener("click", async (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    
    await authenticate(username,password);
    
    if (loginButton.getAttribute('status') === 'True'){
        window.location.href = '/';
        window.location.reload();
    }
    else {
        loginErrorMsg.style.opacity = 1;
    }
});