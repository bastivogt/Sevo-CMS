console.log("Hello from app.js");

function backLink() {
    const backLinks = document.querySelectorAll(".back-link");
    backLinks.forEach((item) => {
        item.addEventListener("click", (e) => {
            e.preventDefault();
            window.history.back();
        });
    });
}
window.addEventListener("DOMContentLoaded", (e) => {
    backLink();
});
