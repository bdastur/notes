function initiate_test_bs_render() {
	console.log("Test suite start");
	body_id = "body";
	var attributes = [];
	var navbar = new NavBar(attributes, body_id, "MyNavBar");

	var item_info = {
		"href": "#",
		"text": "Home"
	};
	navbar.add_nav_link_item(item_info);
	navbar.add_nav_dropdown_item(null);
	dropdown_menu = navbar.add_nav_dropdown_menu("Files");

	item_info = {
		"href": "#",
		"text": "New"
	};
	navbar.add_nav_dropdown_menu_item(dropdown_menu, item_info);

	item_info = {
		"href": "#",
		"text": "Open"
	};
	navbar.add_nav_dropdown_menu_item(dropdown_menu, item_info);

	var accordion = new Accordion("testaccordian", body_id);
    var card_header = {
	    "text": "My collapsible item"
    };
    var card_body = {
	    "id": "collapse1",
	    "text": "This is a test of collapsible item"
    }
    accordion.add_accordion_card("testaccordian", card_header, card_body);

    card_header = {
	    "text": "My another collapsible item"
    };
    var card_body = {
	    "id": "item2",
	    "text": "And here we go again. Yet another test of collapsible item"
    }
    accordion.add_accordion_card("testaccordian", card_header, card_body);




    card_header = {
	    "id": "newheader",
 	    "text": "My very another collapsible item"
    };
    var card_body = {
	    "id": "item3",
	    "text": "And here we go again. Yet another test of collapsible item Blah Blah"
    }

    var card = accordion.add_new_accordian_card();
    accordion.add_new_accordion_card_header(card, "testaccordian1", card_header, card_body);
    var card_body = accordion.add_new_accordion_card_body(card, "testaccordian1", card_body);
    accordion.add_new_accordian_card_menu_item(card_body, "      New menu title");
    accordion.add_new_accordian_card_menu_item(card_body, "      CIS Benchmark - Password check");
    accordion.add_new_accordian_card_menu_item(card_body, "      CIS Benchmark - IAM Policy check");
    accordion.add_new_accordian_card_menu_item(card_body, "      CIS Benchmark - Roles check");


}


function initiate_test() {
    console.log("Test suite start!");

    /************************************************
    // Table rendering tests.
    *************************************************/
    // Render table
    var test_table_id = "table-1";
    var test_container_id = "container-1";
    var rows = [
        ["Jacob", "Dan"],
        ["Alice", " Doe"],
        ["Raj", "Pandya"]
    ];


    var attributes = [
        {"id": "table-1"},
        {"class": "simple sorted"}
    ];

    headers = ["Last Name", "First Name"];

    new_table = new Table(attributes, test_container_id);
    new_table.insert_rows(rows, headers);
    new_table.insert_rows([["Carin", "Durban"]]);

    new_table.sort_by_column(0);



    var heading_attributes = [
	    {"id": "page-heading"}
    ];
    var page_heading = new Heading(heading_attributes, test_container_id, 'h2', "This is a heading");




    /*
    * Button rendering tests
    */
    var button_attributes = [{
        "id": "mybutton-1"
    }];

    var new_button = new Button(button_attributes, "Test Button", test_container_id);

    var button_listener = {
        'event': 'click',
        'callback': function() {
            console.log("Button clicked!");
            new_table.sort_by_column(0);
            page_heading.set_heading_text("This is a new heading now!");
            //sortTable(0, "table-1");
        }
    };
    new_button.add_event_listener(button_listener);
    console.log("Set Button onclick listener!");


    /*
	 * Div test
	*/
	var div_attributes = [
	    {"id": "div-1"},
        {"class": "gelm-1"}
	];
	new_div = new Div(div_attributes, test_container_id);


    /*
	 * List
	*/
	var list_attributes = [
		{"id": "list-1"},
		{"class": "simple_list"}
	];

	var new_list = new List(list_attributes, test_container_id, ordered=true);

	items = [
		"Keeper of the lost cities",
		"Wings of Fire",
		"Magic treehouse"
	]
    new_list.add_list_items(items);
    item_arr = new_list.get_list_items();
    console.log("Item arrr: " + item_arr);

    new_list.delete_list_item_by_idx(2);



    /*
	 * test sorting
	 */
/*
	var arr = [ 2, 4, 1, 54, 3, 5];
	console.log("Array : " + arr);
	arr.sort();
	console.log("Array Sorted: " + arr);

	var names = ["clara", "oak", "ben", "alice"];
    console.log("Array : " + names);
	names.sort();
	console.log("Array Sorted: " + names);


    var arr2 = [
	    ["abc", "cfg", "dfs"],
	    ["ppdd", "uii", "fsdf"],
	    ["nsd", "mrr", "edd"]
    ];
    console.log("Array : " + arr2);
	arr2.sort();
	console.log("Array Sorted: " + arr2);


    arr2.sort(function(a, b) {
	    var valueA = a[1];
	    var valueB = b[1];
	    if (valueA < valueB) {
		    return -1;
	    } else if (valueA > valueB) {
		    return 1;
	    } else {
		    return 0;
	    }

    });



    var newarr = [
	    [1, 2],
	    [3, 4]
    ];

    console.log("NEW ARR: " + newarr[0]);

    var arr3 = [2,  4];
    newarr.push(arr3);
    console.log("NEW ARR: " + newarr[2]);

    console.log("NEW ARR: " + newarr[0]);


*/



}
