
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
        ["Alice", "Doe"],
        ["Raj", "Pandya"]
    ];


    var attributes = [{
	    "id": "table-1"
    }];
    headers = ["Last Name", "First Name"];

    new_table = new Table(attributes, test_container_id);
    new_table.insert_rows(rows, headers);
    new_table.insert_rows([["Carin", "Durban"]]);

    new_table.sort_by_column(0);


    var newarr = [
	    [1, 2],
	    [3, 4]
    ];

    console.log("NEW ARR: " + newarr[0]);

    var arr3 = [2,  4];
    newarr.push(arr3);
    console.log("NEW ARR: " + newarr[2]);


    /*
    * Button rendering tests
    */
    var button_attributes = [{
        "id": "mybutton-1"
    }];

    console.log("NEW ARR: " + newarr[0]);
    var new_button = new Button(button_attributes, "Test Button", test_container_id);

    var button_listener = {
        'event': 'click',
        'callback': function() {
            console.log("Button clicked!");
        }
    };
    new_button.add_event_listener(button_listener);





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
*/



}
