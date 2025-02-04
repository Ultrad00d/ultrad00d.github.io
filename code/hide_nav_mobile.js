function isSmallScreen() {
    return window.matchMedia("(max-width: 1100px)").matches;
}

function handleClick() {
    if (isSmallScreen()) {
        document.getElementById('table-of-contents-active').checked = false;
    }
}

const menuItems = document.querySelectorAll('menu li');

menuItems.forEach(item => {
    item.addEventListener('click', handleClick);
});
