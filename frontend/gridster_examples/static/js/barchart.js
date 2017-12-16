
var BarChart = function generate_new_bar_chart(
    chart_id,
    chart_series,
    chart_title,
    chart_x,
    chart_y)
{
    this.chart_x = chart_x;
    this.chart_y = chart_y;
    this.chart_id = chart_id;
    this.chart_series = chart_series;

    this.chart_type = {
        type: 'bar',
        animation: true,
        backgroundColor: "#e8d04a"
    };

    this.chart_title = {
        text: "AWS Instance Distribution",
        style: {
            color: "#ffffff"
        }
    };

    this.hchart = Highcharts.chart(this.chart_id, {
        chart: this.chart_type,
        title: this.chart_title,
        xAxis: this.chart_x,
        yAxis: this.chart_y,
        series: this.chart_series
    });
}


BarChart.prototype.generate_chart = function(datalist)
{
    console.log("Draw BarChart!")


    for (var i = 0; i < datalist.length; i++) {
        this.hchart.series[i].setData(datalist[i]);
    }
}
