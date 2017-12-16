var testvar = 40;
var refreshInterval = 5;
var myChart;

console.log("this is a js test")

$('#overall_status').text('test')

function getRandom(min, max)
{
    rand = Math.random();
    return Math.floor(rand * (max - min) + min);
}


function draw_col3_rect(){
  var drawing = document.getElementById("col3-rect");
  var con = drawing.getContext("2d");
  //shadow
  con.shadowBlur = 20;
  con.fillStyle = "red";
  con.shadowColor = "blue";
  //rectangle
  con.fillRect(10, 10, 100, 100);
} // end draw


function draw_col1_rect(){
  var drawing = document.getElementById("col1-rect");
  var con = drawing.getContext("2d");
  //shadow
  con.shadowBlur=10;
  con.shadowColor="black";
  //rectangle
  con.fillStyle = "red";
  con.strokeStyle = "white";
  con.fillRect(0, 0, 200, 200);
  //Draw font
  //con.fillStyle = "white"
  //con.lineWidth = "2";
  //con.font = "22pt sans-serif";
  //con.fillText("Canvas Redinging", 5, 90);
  //con.strokeText("Canvas Stroke", 10, 40);
  //con.strokeText("thi sis a test", 10, 70);
  //con.strokeRect(10, 100, 180, 80);
} // end draw


function draw_col2_rect(){
  var drawing = document.getElementById("col2-rect");
  var con = drawing.getContext("2d");
  con.fillStyle = "green";
  con.strokeStyle = "green";
  con.lineWidth = "5";
  con.fillRect(0, 0, 200, 200);
  //con.strokeRect(10, 100, 180, 80);
} // end draw



var barChart = function generate_new_bar_chart(chart_series,
                                        chart_title,
                                        chart_x,
                                        chart_y)
{
    chart_type = {
        type: 'bar',
        animation: true,
        backgroundColor: "#1a0e38"
    };

    return Highcharts.chart('chart-container', {
        chart: chart_type,
        title: chart_title,
        xAxis: chart_x,
        yAxis: chart_y,
        series: chart_series
    });
}




function generate_chart(update_flag)
{
    console.log("Generate Chart!!");

    dev_data = [getRandom(5,30), getRandom(4, 34), getRandom(10, 30)];
    prod_data = [getRandom(3, 30), getRandom(1,20), getRandom(2, 33)];

    chart_series = [
        {
            name: 'Development',
            data:dev_data
        },
        {
            name:'Production',
            data:prod_data
        }
    ];

    chart_type = {
        type: 'bar',
        animation: true,
        backgroundColor: "#1a0e38"
    };

    chart_title = {
        text: "AWS Instance Distribution",
        style: {
            color: "#ffffff"
        }
    };

    chart_x = {
        categories: ['t2.small', 't2.medium', 'm4.large']
    };

    chart_y = {
        title: {
            text: "Instances Running"
        }
    };

    if (update_flag == false) {
        console.log("update flag is false")
        myChart = Highcharts.chart('chart-container', {
            chart: chart_type,
            title: chart_title,
            xAxis: chart_x,
            yAxis: chart_y,
            series: chart_series
        });
    } else {
        console.log("else update!");
        myChart.series[0].setData(dev_data);
        myChart.series[1].setData(prod_data);
    }
}





// An AJAX Wrapper.
function ajaxCall(url,
                  success_callback,
                  error_callback)
{
    $.ajax({
        url: url,
        success: success_callback,
        error: error_callback,
        dataType: "json",
        data: null,
        contentType: "application/json"

    });
}


function ajax_success_handler(data, status, xhr)
{
    console.log("Ajax Success Handler")
    console.log(data)
    console.log(data['key1'])
    console.log(status)
    console.log(getRandom(10, 50))
    $('#overall_status').text(getRandom(99, 434))

}

function ajax_error_handler()
{
    console.log("Ajax Error Handler")
}

function worker()
{
    console.log("Worker invoked")
    ajaxCall("/example1", ajax_success_handler, ajax_error_handler)

}

generate_chart(false);
draw_col1_rect();
draw_col2_rect();
draw_col3_rect();

setInterval(generate_chart, (refreshInterval * 1000), true);

setInterval(worker, (refreshInterval * 1000));
