// static/js/scripts.js
function toggleReview(event) {
    const toggleLink = event.target;
    const reviewText = toggleLink.parentNode;
    const showLess = reviewText.querySelector('.show-less');
    const showMore = reviewText.querySelector('.show-more');

    if (showLess.style.display === 'none') {
        showLess.style.display = 'inline';
        showMore.style.display = 'none';
        toggleLink.textContent = 'Подробнее';
    } else {
        showLess.style.display = 'none';
        showMore.style.display = 'inline';
        toggleLink.textContent = 'Скрыть';
    }
}

function toggleReviewsList(masterId) {
    const reviewsList = document.getElementById(`reviews-list-${masterId}`);
    const toggleLink = document.getElementById(`toggle-link-${masterId}`);

    if (reviewsList.style.display === 'none') {
        reviewsList.style.display = 'block';
        toggleLink.textContent = 'Скрыть отзывы';
    } else {
        reviewsList.style.display = 'none';
        toggleLink.textContent = 'Показать отзывы';
    }
}

function toggleBookingForm() {
    console.log("Toggle function called");
    const bookingForm = document.getElementById('booking-form');
    const toggleButton = document.getElementById('toggle-booking-button');

    if (bookingForm.style.display === 'none') {
        bookingForm.style.display = 'block';
        toggleButton.textContent = 'Скрыть форму записи';
    } else {
        bookingForm.style.display = 'none';
        toggleButton.textContent = 'Записаться';
    }
}

