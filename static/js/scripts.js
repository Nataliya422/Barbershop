document.addEventListener('DOMContentLoaded', function () {
    // Обработчик для переключения видимости отзывов
    document.querySelectorAll('.toggle-review-link').forEach(link => {
        link.addEventListener('click', toggleReview);
    });

    // Обработчик для переключения списка отзывов
    document.querySelectorAll('.toggle-reviews-list').forEach(link => {
        link.addEventListener('click', function(event) {
            const masterId = event.target.dataset.masterId;
            toggleReviewsList(masterId);
        });
    });

    // Обработчик для переключения формы записи
    document.getElementById('toggle-booking-button')?.addEventListener('click', toggleBookingForm);
});

function toggleReview(event) {
    const toggleLink = event.target;
    const reviewText = toggleLink.parentNode;
    const showLess = reviewText.querySelector('.show-less');
    const showMore = reviewText.querySelector('.show-more');

    if (showLess && showMore) {
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
}

function toggleReviewsList(masterId) {
    const reviewsList = document.getElementById(`reviews-list-${masterId}`);
    const toggleLink = document.getElementById(`toggle-link-${masterId}`);

    if (reviewsList && toggleLink) {
        if (reviewsList.style.display === 'none' || reviewsList.style.display === '') {
            reviewsList.style.display = 'block';
            toggleLink.textContent = 'Скрыть отзывы';
        } else {
            reviewsList.style.display = 'none';
            toggleLink.textContent = 'Показать отзывы';
        }
    }
}

function toggleBookingForm() {
    const bookingForm = document.getElementById('booking-form');
    const toggleButton = document.getElementById('toggle-booking-button');

    if (bookingForm && toggleButton) {
        if (bookingForm.style.display === 'none' || bookingForm.style.display === '') {
            bookingForm.style.display = 'block';
            toggleButton.textContent = 'Скрыть форму записи';
        } else {
            bookingForm.style.display = 'none';
            toggleButton.textContent = 'Записаться';
        }
    }
}
