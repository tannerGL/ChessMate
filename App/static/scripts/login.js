const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");


async function authenticate(user, pass)
{
    // return new Promise( () => {
    // $.ajax({
    //     type: "POST",
    //     url: '/attempt_create', 
    //     data: {
    //         username: user,
    //         password: pass,
    //     },
    // success: function(data) {
    //     loginButton.setAttribute('status', data)
    // },
    // })});
    var form = new FormData(loginForm);
    await fetch('/process_creation',
    {
        method: 'POST',
        body: form
    })
    .then((response) => {
        if (!response.ok) 
        {
            throw new Error('Network response was not ok.');
        }
        return response.text();
    })
    .then((response_text) => {
        loginButton.setAttribute('status', response_text);
    })
    .catch((error) => {
        console.error('There has been a problem with your fetch operation:', error);
    });
    
}


loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    
    authenticate(username,password);
    

    if (loginButton.getAttribute('status') === 'True'){
        console.log("made it");
        window.location.href = '/';
        window.location.reload();
    }
    else {
        loginErrorMsg.style.opacity = 1;
    }
});