var userPic = document.getElementsByClassName('user')[0];
var options = document.getElementsByClassName('options')[0];
var userOptionsOpen = false;

window.onclick = function(event) {
    if (event.target != options && event.target != userPic) {
        userOptionsOpen = false;
        options.style.display = "none";
    }
}

userPic.onclick = toggleUserOptions;

function toggleUserOptions() {
    if (userOptionsOpen) {
        userOptionsOpen = false;
        options.style.display = "none";
    } else {
        userOptionsOpen = true;
        options.style.display = "flex";
    }
}
