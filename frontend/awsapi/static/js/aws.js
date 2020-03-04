var data = "test"


function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}


function handle_button_click(button_id) {
	console.log("Button called: " + button_id);
}


async function create_credentials() {
    console.log("Create credentials");
    console.log(window.data)
    data = [
	    ["Behzad", "Dastur"],
	    ["Jack", "Jhonson"],
	    ["David", "Blane"]
    ];
    headers = ["First Name", "Last Name"];
    render_table(headers, data, "container");

    render_table(["cloumn1", "column2"], [], "container", "test-table");

    render_table_row(["John", "Jacobson"], "test-table");
    render_table_row(["Alvin", "Chipmunk"], "test-table");

    // Event:
    var event_listener = {};
    event_listener['event'] = "click";
    event_listener['callback'] = handle_button_click;

    render_button("container", "button-1", event_listener);

    get_session_tokens();
    var i = 0;
    while (i < 3) {
        console.log("Try waiting..")
        await sleep(2000);
        i++;
        console.log("data: " + window.data['api_key']);
    }
    console.log("create_credentials data: " + window.data['api_key'])
    list_s3_buckets();
}


function list_s3_buckets() {
    var creds = new AWS.Credentials(
        window.data['access_key_id'],
        window.data['secret_access_key'],
        window.data['session_token']);

    AWS.config.apiVersions = "2006-03-01";
    AWS.config.credentials = creds;
    AWS.config.region = "us-west-2";

    /*
    var s3 = new AWS.S3();

    var params = {
        Bucket: "beats-logs-dev1",
        MaxKeys: 20
    };
    s3.listObjects(params, function(err, data) {
        if (err) console.log(err, err.stack); // an error occurred
        else console.log(data);           // successful response
    });
    */

    var ec2 = new AWS.EC2();

    var ec2Params = {
        MaxResults: 600
    };

    ec2.describeInstances(ec2Params, function(err, data) {
        if (err) {
            console.log(err, err.stack); // an error occurred
        } else {
            console.log(data);           // successful response
            console.log("Instance id: " + data['Reservations'][0]['Instances'][0]['InstanceId']);
            var table = document.getElementById('instance_table');
            data['Reservations'].forEach((element) => {
                object = element['Instances'][0];
                instance_id = object['InstanceId'];
                instance_type = object['InstanceType'];

                row = table.insertRow();
                var cell = row.insertCell();
                cell.innerHTML = instance_id;
                var cell2 = row.insertCell();
                cell2.innerHTML = instance_type;

            });

        }
    });
}

/*
 * Render a new table.
 *
 * Arguments:
 * headers: list - A list of strings identifying the table headers.
 * rows:    list - A list of list for elements in the table.
 * container_id: string - A dom element identifier for the container of the table.
 * table_id: string - A ddom element identifier to give the table.
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

function render_table_row(row, table_id) {
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




function ajax_success_handler(data, status, xhr)
{
    var curdate = new Date()
    lastupdated_string = curdate.toDateString() + " " +
                         curdate.toTimeString()

    var timeStamp = Math.floor(Date.now() / 1000);
    lastUpdatedTimestamp = timeStamp;

    console.log("Ajax Success Handler: ", curdate.toDateString(),
                "TIME: ", curdate.toTimeString());
    console.log(data);
    window.data = data;
    console.log(status);
    console.log("Window data: ", window.data)
}

function ajax_error_handler(jqXHR, textStatus, errorThrown)
{
    console.log("Ajax Error Handler: ", textStatus, "Error: ", errorThrown);
    console.log("Date: ", Date.now());

    // refresh last updated timestamp
    var timeStamp = Math.floor(Date.now() / 1000);
    var timeDiff = timeStamp - lastUpdatedTimestamp;

    console.log("ERR CALLBACK: Time diff: ", timeDiff);
}

function get_session_tokens()
{
    console.log("Get Session token");
    url = "/credentials"
    ajaxCall(url, ajax_success_handler, ajax_error_handler);
}

