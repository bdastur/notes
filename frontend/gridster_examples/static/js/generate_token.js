$(document).ready(function(){

// Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
//var span = document.getElementsByClassName("close")[0];
var span = document.getElementById("modal-close");


// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    $("div#credentials").text("closed");
    modal.style.display = "none";
}

function generateToken(account, role) {
    alert('button clicked')
}



// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
});

// An AJAX Wrapper.
function ajaxCall(url,
                  success_callback,
                  error_callback)
{
    if (url == undefined || success_callback == undefined
        || error_callback == undefined) {
        console.log("AJAX Call requires url, success \
        callback and error callback");
        return;
    }


    $.ajax({
        url: url,
        success: success_callback,
        error: error_callback,
        dataType: "json",
        data: null,
        contentType: "application/json",
        timeout: (1000 * 1)

    });
}

var creds = document.getElementById("credentials");

function ajax_success_handler(data, status, xhr)
{
    var curdate = new Date()
    lastupdated_string = curdate.toDateString() + " " +
                         curdate.toTimeString()

    var timeStamp = Math.floor(Date.now() / 1000);
    lastUpdatedTimestamp = timeStamp;

    console.log("Ajax Success Handler: ", curdate.toDateString(),
                "TIME: ", curdate.toTimeString());
    console.log(data);
    console.log(data['metric_value']);
    console.log(status);
    //rdeck_statbox.update_message(data['metric_value'], lastupdated_string);
    var txt = document.createTextNode("<p>your cool text</p><p>ANother string</p>");
    console.log(txt)
    $("div#credentials").html(txt.textContent);
}

function ajax_error_handler(jqXHR, textStatus, errorThrown)
{
    console.log("Ajax Error Handler: ", textStatus, "Error: ", errorThrown);
    console.log("Date: ", Date.now());

    // refresh last updated timestamp
    var timeStamp = Math.floor(Date.now() / 1000);
    var timeDiff = timeStamp - lastUpdatedTimestamp;

    console.log("ERR CALLBACK: Time diff: ", timeDiff);
}


function invoke_generate_token_api(account, role)
{
    url = "/generatetoken/account/role"
    ajaxCall(url, ajax_success_handler, ajax_error_handler);
    //rdeck_statbox.update_message(getRandom(20, 100));
}



function generateToken(account, role) {
    var msg = "Button Clicked !" + " - " + account + " : " + role
    alert(msg);
    invoke_generate_token_api(account, role);
}
