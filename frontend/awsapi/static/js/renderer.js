/***************************************************************
 * Bootstrap Navbar manager class.
 *
 ***************************************************************/
class NavBar {
	constructor(attributes, container_id) {
	    this.navbar = document.createElement("nav");

		//Set attributes.
		this.navbar.setAttribute("class", "navbar navbar-expand-lg navbar-dark bg-dark");

        // Navbar Brand.
        var brand = document.createElement("a");
        brand.setAttribute("class", "navbar-brand");
        brand.href = "#";
        brand.innerHTML = "MyNavBar";

        this.navbar.appendChild(brand);

        //Div.
        var nav_div = document.createElement("div");
        nav_div.setAttribute("class", "collapse navbar-collapse");
        nav_div.setAttribute("id", "navbarNav");

        var ul = document.createElement("ul");
        ul.setAttribute("class", "navbar-nav");

        this.ul = ul;

        nav_div.appendChild(ul);
        this.navbar.appendChild(nav_div);

        var container = document.getElementById(container_id);
        container.appendChild(this.navbar);
	}

	add_nav_link_item(item_info) {
        var nav_item = document.createElement("li");
        nav_item.setAttribute("class", "nav-item active");

        var element = document.createElement("a");
        element.setAttribute("class", "nav-link");
        element.href = item_info['href'];
        element.innerHTML = item_info['text'];
        nav_item.appendChild(element);

        this.ul.appendChild(nav_item);
	}

    add_nav_dropdown_menu(menu_heading) {
	    var nav_item = document.createElement("li");
		nav_item.setAttribute("class", "nav-item dropdown");

		var dropdown_toggle = document.createElement("a");
		dropdown_toggle.setAttribute("class", "nav-link dropdown-toggle");
		dropdown_toggle.setAttribute("role", "button");
		dropdown_toggle.setAttribute("data-toggle", "dropdown");
		dropdown_toggle.setAttribute("aria-haspopup", "true");
		dropdown_toggle.setAttribute("aria-expanded", "false");
		dropdown_toggle.href = "#";
		dropdown_toggle.innerHTML = menu_heading;

		nav_item.appendChild(dropdown_toggle);

		var dropdown_menu = document.createElement("div");
		dropdown_menu.setAttribute("class", "dropdown-menu");
		dropdown_menu.setAttribute("aria-labelledby", "navbarDropdown");

		nav_item.appendChild(dropdown_menu);

		this.ul.appendChild(nav_item);
    }



	add_nav_dropdown_item(item_info) {
		var nav_item = document.createElement("li");
		nav_item.setAttribute("class", "nav-item dropdown");

		var dropdown_toggle = document.createElement("a");
		dropdown_toggle.setAttribute("class", "nav-link dropdown-toggle");
		dropdown_toggle.setAttribute("role", "button");
		dropdown_toggle.setAttribute("data-toggle", "dropdown");
		dropdown_toggle.setAttribute("aria-haspopup", "true");
		dropdown_toggle.setAttribute("aria-expanded", "false");
		dropdown_toggle.href = "#";
		dropdown_toggle.innerHTML = "Dropdown Menu";

		nav_item.appendChild(dropdown_toggle);

		var dropdown_menu = document.createElement("div");
		dropdown_menu.setAttribute("class", "dropdown-menu");
		dropdown_menu.setAttribute("aria-labelledby", "navbarDropdown");

		nav_item.appendChild(dropdown_menu);

        var ddmenu_item = document.createElement("a");
        ddmenu_item.setAttribute("class", "dropdown-item");
        ddmenu_item.href = "#";
        ddmenu_item.innerHTML = "Menu item";

        dropdown_menu.appendChild(ddmenu_item);

        this.ul.appendChild(nav_item);
	}
 }



/***************************************************************
 * DIV.
 * Manage DOM element div.
 * HTML Block level element. (Grouping element)
 ***************************************************************/
class Div {
	constructor(attributes, container_id) {
		this.div = document.createElement("div");

		attributes.forEach((attribute) => {
            var key = Object.keys(attribute);
            var value = attribute[key];
            this.div.setAttribute(key, value);
        });

        var container = document.getElementById(container_id);
        container.appendChild(this.div);
	}

    add_text(text) {
	    this.div.innerHTML = text;
    }

	remove_child(child_id) {
		var child = document.getElementById(child_id);
		this.div.removeChild(child);
	}

}


/***************************************************************
 * Heading.
 * Manage DOM element h1..h6
 *
 ***************************************************************/
class Heading {
	constructor(attributes, container_id, heading_level, heading_text) {
		this.heading = document.createElement(heading_level);

		attributes.forEach((attribute) => {
            var key = Object.keys(attribute);
            var value = attribute[key];
            this.heading.setAttribute(key, value);
        });
        this.heading.innerHTML = heading_text;

        var container = document.getElementById(container_id);
        container.appendChild(this.heading);
	}

	set_heading_text(heading_text) {
		this.heading.innerHTML = heading_text;
	}


}


/***************************************************************
 * List.
 * Manage DOM element ol or ul (Ordered or Unordered list).
 *
 ***************************************************************/
class List {
	constructor(attributes, container_id, ordered=true) {
		this.ordered = ordered;
		if (ordered == true) {
			this.list = document.createElement("ol");
		} else {
			this.list = document.createElement("ul");
		}

		attributes.forEach((attribute) => {
            var key = Object.keys(attribute);
            var value = attribute[key];
            this.list.setAttribute(key, value);
        });

        var container = document.getElementById(container_id);
        container.appendChild(this.list);
	}

	add_list_items(items) {
		items.forEach((item) => {
			var item_obj = document.createElement("li");
			item_obj.innerHTML = item;
			this.list.appendChild(item_obj);
		});
	}

	get_list_items() {
		var item_array = []
		// This returns an HTMLCollection object
		var items = this.list.getElementsByTagName("li");


        // This is how to iterate an HTMLCollection object
		for (var item of items) {
			item_array.push(item.innerHTML);
		}

		return item_array;
	}

    delete_list_item_by_idx(item_idx) {
	    var item = this.list.getElementsByTagName("li")[item_idx];
	    this.list.removeChild(item);
    }

}





/***************************************************************
 * Button.
 * Manage DOM element button.
 *
 ***************************************************************/
class Button {
	/*
     * Construct
     * Construct a new Button object.
     *
     * Arguments:
     * attributes - hash - A key/value pair of attributes to set to the table
     * html_text - string - Button text
     * container_id- string - DOM ID of the container to put the table element in.
	 */
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




/****************************************************************
 * Table class.
 * Manage DOM element table.
 ****************************************************************/
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
			console.log("Attribute key: " + key + ", value: " + value);
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

            /*
             * what's the purpose of const $this = this.
             * https://stackoverflow.com/questions/43642729/calling-a-method-from-another-method-in-the-same-class
             */
            const $this = this;

            var col_idx = 0;
            headers.forEach((element) => {
	            var th = document.createElement("th");
	            th.onclick = sortTable(col_idx.toString(2), $this.table.id);
	            th.setAttribute("id", $this.table.id + "_th__" + col_idx);


	            th.addEventListener("click", function(ev) {
                    //console.log("EV: " + ev.target.id);
                    var cellidx = ev.target.id.split("__")[1];
                    sortTable(cellidx, $this.table.id);
	            });


	            th.innerHTML = element;
	            thead_row.appendChild(th);
	            col_idx++;
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


function sortTable(n, table_id) {
  console.log("sortTable: col: " + n + "Table id: " + table_id);
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById(table_id);
  if (table == null) {
	  return;
  }
  switching = true;
  // Set the sorting direction to ascending:
  dir = "asc";
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < (rows.length - 1); i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount ++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}







