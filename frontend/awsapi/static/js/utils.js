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

