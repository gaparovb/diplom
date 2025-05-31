document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('http://127.0.0.1:8000/auth/jwt/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();
    const messageDiv = document.getElementById('message');

    if (response.ok) {
        messageDiv.innerText = 'Login successful!';
        localStorage.setItem('access', data.access);
        localStorage.setItem('refresh', data.refresh);
        // перенаправление после входа
        window.location.href = 'articles.html';
    } else {
        messageDiv.innerText = data.detail || 'Login failed';
    }
});
