function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie != '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function save(form) {
    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getToken('csrftoken'),
        },
        body: new FormData(form)
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            alert(data.message)
        })
        .catch(alert);
}
