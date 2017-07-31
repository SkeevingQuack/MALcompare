function getUserList() {
    var malName = document.forms["mainForm"]["malName"].value;

    // var xhr = new XMLHttpRequest();
    // var requestUrl = "http://myanimelist.net/malappinfo.php?u=" + malName + "&status=all&type=anime";
    // xhr.open("GET", requestURL, false);
    // xhr.send();

    var userListDisplay = document.getElementById("userList");
    //   userListDisplay.innerHTML = xhr.responseText;
    userListDisplay.innerHTML = malName;

    return false;
}

function test() {
    alert('sdfojsdf');
}
