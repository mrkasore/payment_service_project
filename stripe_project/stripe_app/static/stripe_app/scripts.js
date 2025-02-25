document.addEventListener('DOMContentLoaded', function() {
    var buyButton = document.getElementById('buy-button');
    var stripePublicKey = buyButton.getAttribute('data-stripe-key');
    var itemId = buyButton.getAttribute('data-item-id');
    var csrftoken = buyButton.getAttribute('data-csrf-token');
    var stripe = Stripe(stripePublicKey);

    if (buyButton) {
        buyButton.addEventListener('click', function() {
            fetch('/buy/' + itemId + '/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                })
                .then(response => response.json())
                .then(session => {
                    return stripe.redirectToCheckout({ sessionId: session.session_id });
                })
                .then(result => {
                    if (result.error) {
                        alert(result.error.message);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}