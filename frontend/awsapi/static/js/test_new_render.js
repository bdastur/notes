
function initiate_test() {
    console.log("Test3: Test suite start!");


    body = document.getElementById("body");
    console.log("Body: " + body);

    // Create a nav bar.
    var navbar = new NavBar(undefined, "body", "Banner");
    navbar.add_nav_link_item({"href": "https://google.com", "text": "Home"});

    // Define a heading.
    h2elem = new HTMLElement("h2");
    h2elem.set_text("This is a new text! <kbd>ctrl</kbd>  + <kbd>,</kbd>");
    h2elem.set_parent(body);
    h2elem.set_attributes("class", "h2");


    //Define a list group
    var list_elem = new HTMLElement("ul");
    list_elem.set_attributes("class", "list-group");
    list_elem.set_parent(body);

    var no_of_items = 5;
    var list_items = []
    for (var idx = 0; idx < no_of_items; idx++) {
	    list_items[idx] = new HTMLElement("li");
        list_items[idx].set_attributes("class", "list-group-item");
        list_items[idx].set_text("This is a test!");
        list_elem.add_child(list_items[idx]);
    }



}
