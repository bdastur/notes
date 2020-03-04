
/*
 * Render a new table.
 *
 * Arguments:
 * headers: list - A list of strings identifying the table headers.
 * rows:    list - A list of rows with elements to insert in cells in the table.
 * container_id: string - A dom element identifier for the container of the table.
 * table_id: string - A dom element identifier to give the table.
 *
*/
function render_table(headers, rows, container_id, table_id) {
	div_obj = document.getElementById(container_id);
	table = document.createElement("table");
	console.log("Table id: " + table_id);
	if (table_id == undefined) {
		table_id = "table" + Math.round((Math.random() * 10000));
	}

	console.log("Table id: " + table_id);

	table.setAttribute("id", table_id);


    // Create a table header.
    var thead = table.createTHead();
    var thead_row = table.insertRow();
    headers.forEach((element) => {
	    var th = document.createElement("th");
	    th.innerHTML = element;
	    thead_row.appendChild(th);
    });


    rows.forEach((row) => {
	    rowobj = table.insertRow();

	    row.forEach((item) => {
	        var cell = rowobj.insertCell();
	        cell.innerHTML = item;
	    });

    });

	div_obj.appendChild(table);
}


/*
 * Insert a new row to an existing table.
 *
 * Arguments:
 * row - list - A list of elements of the row
 * table_id - string - A dom element identifier for the table.
 */
function render_table_insert_row(row, table_id) {
	table = document.getElementById(table_id);
	var rowobj = table.insertRow();
	row.forEach((item) => {
		var cell = rowobj.insertCell();
		cell.innerHTML = item;
	});

}



function render_button(container_id, button_id, event_listener) {
	var container_obj = document.getElementById(container_id);
	var button = document.createElement("button");
	button.innerHTML = "Submit";
	button.setAttribute("id", button_id);

	// Add event listener.
	if (event_listener != undefined) {
        button.addEventListener(event_listener['event'], event_listener['callback']);
    }

	container_obj.appendChild(button);
}




/*
 * Table class.
 * Manage DOM element table.
 */
class Table {
    /*
	 * Constructor.
	 * construct a new Table object
	 *
	 * Arguments:
	 * attributes - hash - A key/value pair of attributes to set to the table.
	 * container_id - string - DOM ID of the container to put the table element in.
	 *
	 * usage: new_table = new Table([{"id": "table-1"}], "container-1");
	 */
	constructor(attributes, container_id) {
		this.attributes = attributes;
		this.table = document.createElement("table")
		attributes.forEach((attribute) => {
			var key = Object.keys(attribute);
			var value = attribute[key];
			table.setAttribute(key, value);
		});

		var container = document.getElementById(container_id);
		container.appendChild(this.table);
	}

    /*
	 * insert_rows.
	 * Insert new rows to the table.
	 *
	 * Arguments:
	 * rows - list of list - A list of rows to add to the table.
	 * headers - list (optional) - to set the table header.
	 */
	insert_rows(rows, headers) {
	    if (headers != undefined) {
		    // Create a table header.
            var thead = this.table.createTHead();
            var thead_row = this.table.insertRow();
            headers.forEach((element) => {
	            var th = document.createElement("th");
	            th.innerHTML = element;
	            thead_row.appendChild(th);
            });
        }

        rows.forEach((row) => {
	        rowobj = this.table.insertRow();

	        row.forEach((item) => {
	            var cell = rowobj.insertCell();
	            cell.innerHTML = item;
	        });

        });
	}
}





