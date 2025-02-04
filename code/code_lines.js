document.addEventListener("DOMContentLoaded", function() {
    // Подсветка синтаксиса
    const codeBlocks = document.querySelectorAll('pre code.hljs');

    codeBlocks.forEach((block) => {
        // Подсветка синтаксиса
        hljs.highlightBlock(block);

        // Получаем текст и разбиваем на строки
        const lines = block.innerText.split('\n');
        // Обновляем содержимое с добавлением номеров строк
        block.innerHTML = lines.map(line => `<span class="line">${line}</span>`).join('');
    });
});
