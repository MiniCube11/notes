var flashMessage = document.getElementsByClassName('flash-message')[0];
var closeButton = document.getElementById('close-button');

closeButton.onclick = closeMessage;

function closeMessage() {
    flashMessage.style.display = "none";
}
