
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
    console.log("AJAX Call invoked.")

    $.ajax({
        url: url,
        success: success_callback,
        error: error_callback,
        dataType: "json",
        data: null,
        method: "POST",
        contentType: "application/json",
        timeout: (10000 * 1)

    });
}

function ajax_success_handler(data, status, xhr)
{
    var curdate = new Date()
    lastupdated_string = curdate.toDateString() + " " +
                         curdate.toTimeString()

    var timeStamp = Math.floor(Date.now() / 1000);

    console.log("Ajax Success Handler: ", curdate.toDateString(),
                "TIME: ", curdate.toTimeString());
    console.log(data);
    console.log(data['metric_value']);
    console.log(status);

    //$("div#credentials").html(msg);

}

function ajax_error_handler(jqXHR, textStatus, errorThrown)
{
    console.log("Ajax Error Handler: ", textStatus, "Error: ", errorThrown);
    console.log("Date: ", Date.now());

    // refresh last updated timestamp

    console.log("ERR CALLBACK: Time diff: ");
}


function invoke_flask_post()
{
    alert("invoke flask post");
    url = "/forms/formhandle";
    console.log("make ajaxCall");
    ajaxCall(url, ajax_success_handler, ajax_error_handler);
}


function submitForm() {
    alert("form clicked!")
    console.log("Clicked..");
    invoke_flask_post();
}
