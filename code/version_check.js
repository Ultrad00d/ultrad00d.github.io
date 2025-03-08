const appVersion = '1.0.0';

function updateVersion() {
    const versionElements = document.querySelectorAll('.versjs');
    versionElements.forEach(element => {
        element.textContent = appVersion;
    });
}
updateVersion();

const notification = document.getElementById('new-version-container');
const closeButton = document.getElementById('hideUpdate');

const savedVersion = localStorage.getItem('appVersion');
const isNotificationHidden = localStorage.getItem('notificationHidden') === 'true';

if (savedVersion !== appVersion) {
    notification.style.display = 'flex';
} else if (isNotificationHidden) {
    notification.style.display = 'none';
}

closeButton.addEventListener('click', function() {
    notification.classList.add('hidden');
    setTimeout(() => {
        notification.style.display = 'none';
    }, 300);
    localStorage.setItem('notificationHidden', 'true');
});

localStorage.setItem('appVersion', appVersion);
