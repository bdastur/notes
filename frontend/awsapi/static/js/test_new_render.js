
function initiate_test() {
    console.log("Test3: Test suite start!");


    body = document.getElementById("body");
    console.log("BOdy: " + body);

    // Define a heading.
    h2elem = new HTMLElement("h2");
    h2elem.set_text("This is a new text! <kbd><kbd>ctrl</kbd> + <kbd>,</kbd></kbd>");
    h2elem.set_parent(body);
    h2elem.set_attributes("class", "h2");




}
