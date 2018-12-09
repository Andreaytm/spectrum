/* adapted from www.w3schools.com */
window.onscroll = function () {
    scrollToTop();
};

function scrollToTop() {
    if (document.body.scrollTop > 10 || document.documentElement.scrollTop > 10) {
        document.getElementById("toTopBtn").style.display = "block";
    } else {
        document.getElementById("toTopBtn").style.display = "none";
    }
}

// When the user clicks on button scroll to the top of the page
function GoToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}