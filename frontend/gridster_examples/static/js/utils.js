
console.log("this is the utils file")


function add_text(con, x_pos, y_pos, color, fontstyle, msg)
{

    /* Add Text */
    con.fillStyle = color;
    con.lineWidth = "2";
    con.font = fontstyle;
    con.textAlign = "center";
    con.fillText(msg, x_pos, y_pos);
}


/*
 * A simple function which returns a random value
 * between the min and max range.
 */
function getRandom(min, max)
{
    rand = Math.random();
    return Math.floor(rand * (max - min) + min);
}

function default_error_callback()
{
    console.log("Callback Failed");
}

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
