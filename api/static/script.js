let isActive = false;

document.getElementById('submitBtn')?.addEventListener('click', function(e) {
    if (!isActive) {
        e.preventDefault();
        return;
    }

    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    // Client-side validation fallback
    if (user === '' || pass === '') {
        e.preventDefault();
        document.getElementById('errorMsg').innerText = "Username and password are required.";
    }
});