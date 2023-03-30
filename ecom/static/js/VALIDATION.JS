function equalpassword() {
    let passwordInput = document.getElementById('password');
    let confirmPasswordInput = document.getElementById('confirm-password');

    let password = passwordInput.value;
    let confirmPassword = confirmPasswordInput.value;

    if (password === confirmPassword) {
        setSuccess(passwordInput);
    } else {
        setError(confirmPasswordInput, 'Passwords do not match.');
    }
}

function setError(input, message) {
    let submitbutton = document.getElementById("button")
    const formcontrol = input.parentElement;
    const small = formcontrol.querySelector('small');
    small.className = 'smallshown';
    small.innerText = message;
    submitbutton.disabled = true
}

function setSuccess(input) {
    let submitbutton = document.getElementById("button")
    const formcontrol = input.parentElement;
    const small = formcontrol.querySelector('small');
    small.className = 'smallhidden';
    small.innerText = "";
    submitbutton.disabled = false
}