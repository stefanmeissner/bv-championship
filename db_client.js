function getFileFromServer(url, doneCallback) {
    var xhr;

    xhr = new XMLHttpRequest();
    xhr.onreadystatechange = handleStateChange;
    xhr.open("GET", url, true);
    xhr.send();

    function handleStateChange() {
        if (xhr.readyState === 4) {
            doneCallback(xhr.status == 200 ? xhr.responseText : null);
        }
    }
}

function init() {
    getFileFromServer("https://raw.githubusercontent.com/RobertPazurek/bv-championship/master/points_meisi.txt", function(text) {
        if (text === null) {
            // An error occurred
        }
        else {
            document.getElementById("points_meisi").innerHTML = text + ' <i class="tui-icon tui-icon--certificate"></i>';
        }
    });

    getFileFromServer("https://raw.githubusercontent.com/RobertPazurek/bv-championship/master/points_rob.txt", function(text) {
        if (text === null) {
            // An error occurred
        }
        else {
            document.getElementById("points_rob").innerHTML = text + ' <i class="tui-icon tui-icon--certificate"></i>';
        }
    });
}


document.addEventListener('DOMContentLoaded', init, false);
