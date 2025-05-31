async function fetchArticles() {
    const token = localStorage.getItem('access');

    const response = await fetch('http://127.0.0.1:8000/api/articles/', {
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const articles = await response.json();
        const container = document.getElementById('articles-container');
        container.innerHTML = '';

        articles.forEach(article => {
            const div = document.createElement('div');
            div.className = 'article';
            div.innerHTML = `<h3>${article.title}</h3><p>${article.content}</p>`;
            container.appendChild(div);
        });
    } else {
        alert('Failed to load articles');
    }
}

function logout() {
    localStorage.removeItem('access');
    window.location.href = 'login.html';
}

fetchArticles();
