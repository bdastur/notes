function ClickHandler(buttonName) {
    msg = "Button " + buttonName + " pressed!"
    console.log(msg)
    var printarea  = $("#print")
    printarea.html(msg)
    var myButton = $("#defaultbutton")
    if (myButton.length) {
        myButton.removeClass('btn-default').addClass('btn-danger')
    } else {
        console.log("Cannot find defaultbutton")
    }

    console.log("Update button class!")
}


function EventHandler(type, name) {
    msg = "Event from " + name + " of type " + type
    console.log(msg)
    if (type == "textarea") {
        console.log("This is a textarea")
        var x = document.getElementById(name).value;
        console.log(x)
        var id = "#" + name
        var myobj = $("#mytextarea")
        var myval = myobj.value
        console.log(myval)
    }

}

