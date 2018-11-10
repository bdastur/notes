function ClickHandler(buttonName) {
    msg = "Button " + buttonName + " pressed!"
    console.log(msg)
    var printarea  = $("#print")
    printarea.html(msg)
}


