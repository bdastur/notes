
var refreshInterval = 5;
var lastUpdatedTimestamp = 0;

/*
 * Set Chart dev_data
 */
dev_data = [getRandom(5,30), getRandom(4, 34), getRandom(10, 30)];
prod_data = [getRandom(3, 30), getRandom(1,20), getRandom(2, 33)];
myseries = [
    {
        name: 'Development',
        data:dev_data
    },
    {
        name:'Production',
        data:prod_data
    }
];


mytitle = {
    text: "AWS Instance Distribution",
    style: {
        color: "#ffffff"
    }
};

mychart_x = {
    categories: ['t2.small', 't2.medium', 'm4.large']
};

mychart_y = {
    title: {
        text: "Instances Running"
    }
};

/*
 * Initialize BarChart.
 */
var mychart = new BarChart("chart-container",
myseries,
mytitle,
mychart_x,
mychart_y);


function regenerate_chart()
{
    datalist = [[getRandom(5,30), getRandom(4, 34), getRandom(10, 30)],
     [getRandom(3, 30), getRandom(1,20), getRandom(2, 33)]];
    mychart.generate_chart(datalist);
}


/*
 * Initalize an object of type SingleStatGridbox as below.
 * Note: Do not forget the keyword new.
 */
var rdeck_statbox = new SingleStatGridbox("rdeck-availability",
                                      "Rundeck Availability",
                                       0);

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
    console.log(data['metric_value']);
    console.log(status);
    rdeck_statbox.update_message(data['metric_value'], lastupdated_string);

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

function update_rdeck_metric()
{
    url = "/rundeckstat"
    ajaxCall(url, ajax_success_handler, ajax_error_handler);
    //rdeck_statbox.update_message(getRandom(20, 100));
}

/*
 * To add a multiline text
 * use the html() function instead of text()
 */
var msg = "This is a test" + "\n" + "<p>test</p>" +  "Another line";
console.log("msg: ", msg);

var myelem = $('.gridster #box21').html(msg);
console.log("myelem text: ", myelem);


var mystyles = $('#box21').css('background');

console.log("Background color: ", mystyles);
console.log("Set backgroud color");
/*
 * Change the backgroud Color of the element with
 * id box21, which has a parent element with class
 * gridster
 */
$('.gridster #box21').css({backgroundColor: 'blue'});


/*
for (var property in mystyles) {
    console.log("Property: ", property, "  Value: ", mystyles[property]);
}
*/

setInterval(update_rdeck_metric, (refreshInterval * 1000));
setInterval(regenerate_chart, (refreshInterval * 1000));
