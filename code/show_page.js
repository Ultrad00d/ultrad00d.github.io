const pageButtons = document.querySelectorAll('input[name="pageNumber"]');

function updateActiveClass() {
    pageButtons.forEach(radio => {
        const label = radio.closest('.pageRadio');
        const contentElement = document.getElementById(`content${radio.id}`);
        const summaryElement = document.getElementById(`summary${radio.id}`);
        const tutorContainer = document.getElementById('tutorContainer');
        document.getElementById('table-of-contents-active').checked = true;
        if (radio.checked) {
            label.classList.add('active');
            contentElement.classList.add('visible');
            summaryElement.classList.add('visible');
        } else {
            label.classList.remove('active');
            contentElement.classList.remove('visible');
            summaryElement.classList.remove('visible');
            tutorContainer.classList.remove('visible');
        }
    });
}

pageButtons.forEach(radio => {
    radio.addEventListener('click', updateActiveClass);
});