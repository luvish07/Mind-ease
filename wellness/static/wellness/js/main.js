function startBreathing(button, circle) {
    button.innerHTML = "Breathing active... Follow the circle.";
    circle.style.width = "120px";
    circle.style.height = "120px";
    circle.textContent = "Breathe In";

    window.setTimeout(() => {
        circle.textContent = "Hold";

        window.setTimeout(() => {
            circle.style.width = "0px";
            circle.style.height = "0px";
            circle.textContent = "";
            button.innerHTML = "Start Exercise <span class=\"ml-2\">-&gt;</span>";
        }, 4000);
    }, 4000);
}

document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector("[data-breath-button]");
    const circle = document.querySelector("[data-breath-circle]");

    if (button && circle) {
        button.addEventListener("click", () => startBreathing(button, circle));
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
