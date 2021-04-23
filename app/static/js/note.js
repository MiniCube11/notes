var userPic = document.getElementsByClassName('user')[0];
var options = document.getElementsByClassName('options')[0];
var userOptionsOpen = false;

var noteMenu = document.getElementsByClassName('note-menu')[0];
var noteOptions = document.getElementsByClassName('note-options')[0];
var noteMenuOpen = false;

var deleteLink = document.getElementById('delete');
var modal = document.getElementsByClassName('delete-note-modal')[0];
var modalBackground = document.getElementsByClassName('modal-background')[0];
var cancelButton = document.getElementsByTagName('button')[0];
var deleteButton = document.getElementsByTagName('button')[1];
var modalOpen = false;

window.onclick = function(event) {
    if (event.target != options && event.target != userPic) {
        userOptionsOpen = false;
        options.style.display = "none";
    }
    if (event.target != noteOptions && event.target != noteMenu) {
        noteMenuOpen = false;
        noteOptions.style.display = "none";
    }
    if (event.target == modalBackground || event.target == cancelButton) {
        modalOpen = false;
        modal.style.display = "none";
        modalBackground.style.display = "none";
    }
}

userPic.onclick = toggleUserOptions;
noteMenu.onclick = toggleMenuOpen;

function toggleUserOptions() {
    if (userOptionsOpen) {
        userOptionsOpen = false;
        options.style.display = "none";
    } else {
        userOptionsOpen = true;
        options.style.display = "flex";
    }
}

function toggleMenuOpen() {
    if (noteMenuOpen) {
        noteMenuOpen = false;
        noteOptions.style.display = "none";
    } else {
        noteMenuOpen = true;
        noteOptions.style.display = "flex";
    }
}

function toggleModal() {
    if (modalOpen) {
        modalOpen = false;
        modal.style.display = "none";
        modalBackground.style.display = "none";
    } else {
        modalOpen = true;
        modal.style.display = "flex";
        modalBackground.style.display = "block";
    }
}
