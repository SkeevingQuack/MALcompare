var apiUrl = '';

function getUserList() {
    var malName = document.forms["mainForm"]["malName"].value;

    var xhr = new XMLHttpRequest();

    xhr.open("GET", requestUrl, false);
    xhr.send();

    var userListDisplay = document.getElementById("userList");
    userListDisplay.innerHTML = xhr.response + "\n" + xhr.responseText;

    return false;
}
