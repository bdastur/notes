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

generate_chart(false)

setInterval(generate_chart, (refreshInterval * 1000), true);

setInterval(worker, (refreshInterval * 1000));
