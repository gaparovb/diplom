// frontend/js/auth.js
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const response = await fetch('http://127.0.0.1:8000/auth/jwt/create/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            username: document.getElementById('username').value,
            password: document.getElementById('password').value
        })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem('access', data.access);
        window.location.href = 'articles.html';
    } else {
        alert('Login failed');
    }
});
