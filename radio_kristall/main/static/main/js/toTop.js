// Получаем кнопку по её ID
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Функция, которая показывает или скрывает кнопку в зависимости от положения скролла
function toggleScrollButton() {
    if (window.scrollY > 300) { // Если прокрутили больше чем на 300px
        scrollToTopBtn.classList.add("show");
    } else {
        scrollToTopBtn.classList.remove("show");
    }
}

// Функция для плавного скролла наверх
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth" // Плавная прокрутка
    });
}

// Следим за событием прокрутки, чтобы вызвать функцию показа/скрытия
window.addEventListener("scroll", toggleScrollButton);

// При клике на кнопку вызываем скролл наверх
scrollToTopBtn.addEventListener("click", scrollToTop);