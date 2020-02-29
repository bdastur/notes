var data = "test"

function sleep (time) {
  return new Promise((resolve) => setTimeout(resolve, time));
}

async function create_credentials() {
    console.log("Create credentials");
    console.log(window.data)
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
        }
    });
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

