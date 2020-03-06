
class Button {
    constructor(attributes, html_text, container_id) {
        this.button = document.createElement("button");
        this.button.innerHTML = html_text;

        attributes.forEach((attribute) => {
            var key = Object.keys(attribute);
            var value = attribute[key];
            this.button.setAttribute(key, value);
        });

        var container = document.getElementById(container_id);
        container.appendChild(this.button);
    }

    add_event_listener(event_listener) {
        if (event_listener == undefined) {
            console.log("Event listener is undefined, Do nothing!");
            return;
        }
        this.button.addEventListener(event_listener['event'], event_listener['callback']);
    }

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
		this.rows = [];
		this.attributes = attributes;
		this.table = document.createElement("table");
		this.header_on = false;

		attributes.forEach((attribute) => {
			var key = Object.keys(attribute);
			var value = attribute[key];
			this.table.setAttribute(key, value);
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
		    this.header_on = true;
            var thead = this.table.createTHead();
            var thead_row = this.table.insertRow();
            headers.forEach((element) => {
	            var th = document.createElement("th");
	            th.innerHTML = element;
	            thead_row.appendChild(th);
            });
        }

        rows.forEach((row) => {
	        this.rows.push(row);
	        var rowobj = this.table.insertRow();

	        row.forEach((item) => {
	            var cell = rowobj.insertCell();
	            cell.innerHTML = item;
	        });
        });

        console.log("Rows: --> " + this.rows[1]);
	}


    sort_by_column(column_idx) {
        if (column_idx == undefined) {
	        column_idx = 0;
        }
        console.log("Before This rows: : : " + this.rows[2] + " len: " + this.rows.length);

        this.rows.sort(function(a, b) {
	        var valueA = a[column_idx];
	        var valueB = b[column_idx];
	        if (valueA < valueB) {
		        return -1;
	        } else if (valueA > valueB) {
		        return 1;
	        } else {
		        return 0;
	        }
        });

        var start_idx = 0;
        if (this.header_on == true) {
	        start_idx = 1;
        }
        var row_count = 0;
        console.log("Ater This rows: : : " + this.rows + " len: " + this.rows.length);
        for (var idx = start_idx, row; row = this.table.rows[idx]; idx++, row_count++) {
	        for(var j = 0, col; col = row.cells[j]; j++) {
	            console.log("COL: " + col);
	            col.innerHTML = this.rows[row_count][j];
	        }
        }
    }
}





