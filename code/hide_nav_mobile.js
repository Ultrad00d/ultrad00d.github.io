function resetCheckbox() {
    document.getElementById('table-of-contents-active').checked = false;
}

function isSmallScreen() {
    return window.matchMedia("(max-width: 1100px)").matches;
}

function handleClick() {
    if (isSmallScreen()) {
        resetCheckbox();
    }
}

const menuItems = document.querySelectorAll('menu li');

menuItems.forEach(item => {
    item.addEventListener('click', handleClick);
});
document.addEventListener('DOMContentLoaded', resetCheckbox);
