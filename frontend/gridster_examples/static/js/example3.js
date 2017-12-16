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


var SingleStatWidget = function(div_id, widget_color, pos_x, pos_y)
{
    /*
     * Validate Arguments.
     */
    if (div_id == undefined || widget_color == undefined) {
        console.log("Arguments are not defined")
        return null;
    }

    if (pos_x == undefined) {
        this.pos_x = 5;
    }

    if (pos_y == undefined) {
        this.pos_y = 5;
    }
    this.fill_x = 210;
    this.fill_y = 210;

    this.div_id = div_id;
    this.widget_color = widget_color;

    /* Draw the widget */
    this.drawing = document.getElementById(this.div_id);
    this.con = this.drawing.getContext("2d");

    this.con.shadowBlur = 20;
    this.con.fillStyle = this.widget_color;
    this.con.shadowColor = "black";
    this.con.fillRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);

    console.log("SingleStatWidget Initalized.", this.div_id, ": color",
                this.widget_color);
}

SingleStatWidget.prototype.draw_widget = function()
{
    console.log("Draw Widget invoked.")
    this.con.fillStyle = this.widget_color;
    this.con.shadowBlur = 10;
    this.con.shadowColor = "gray"
    this.con.fillRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);
}


SingleStatWidget.prototype.set_text = function(msg, fontstyle)
{
    /* Overwrite text */
    this.con.clearRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);
    this.draw_widget();

    this.con.lineWidth = "2";
    x_pos = this.pos_x + this.fill_x/2;
    y_pos = this.pos_y + this.fill_y/2;
    this.con.textAlign = "center"
    if (fontstyle == undefined) {
        this.con.font = "12pt sans-serif";
    } else {
        this.con.font = fontstyle;
    }

    this.con.shadowBlur = 0;
    /* add new text in same location */
    this.msg = msg;
    this.con.fillStyle = "yellow";
    this.con.fillText(msg, x_pos, y_pos);
}

function add_text(con, x_pos, y_pos, color, fontstyle, msg)
{
    console.log("Widget color: ", con.widget_color);
    con.fillStyle = con.widget_color;
    /* Add Text */
    con.msg = msg;
    con.fillStyle = color;
    con.lineWidth = "2";
    con.font = fontstyle;
    con.textAlign = "center";
    con.fillText(msg, x_pos, y_pos);
}



function draw_col3_rect(){
  var drawing = document.getElementById("col3-rect");
  var con = drawing.getContext("2d");
  //shadow
  con.shadowBlur = 20;
  con.fillStyle = "red";
  con.shadowColor = "black";
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
  con.fillRect(0, 0, 200, 2000);
  //con.strokeRect(10, 100, 180, 80);
} // end draw


function draw_fullrow_rect(){
  var drawing = document.getElementById("full-row");
  var con = drawing.getContext("2d");

  rect_count = 3;
  rect_start_x = 10;
  rect_start_y = 10;
  rect_fill_x = 180;
  rect_fill_y = 180;
  rect_fill_shadow = 15;
  rect_gap = 15;

  con.shadowBlur = rect_fill_shadow;
  con.fillStyle = "#ff1c1c";
  con.shadowColor = "#19191c";

  con.fillRect(rect_start_x, rect_start_y, rect_fill_x, rect_fill_y);

  for (i = 1; i < rect_count; i++) {
      rect_start_x += rect_fill_x + rect_gap
      con.fillRect(rect_start_x, rect_start_y, rect_fill_x, rect_fill_y);

  }

  /* Add Text */
  rect_start_x = 10;

  con.fillStyle = "yellow";
  con.lineWidth = "2";
  con.font = "14pt sans-serif";
  con.textAlign = "center";

  con.fillText("AWS S3 Service",
               (rect_start_x + rect_fill_x/2),
               (rect_start_y + rect_fill_y/2));
  con.font = "18pt sans-serif";
  con.fillText("100%",
               (rect_start_x + rect_fill_x/2),
               (rect_start_y + rect_fill_y/2 + 50));

for (var i = 1; i < rect_count; i++) {
    rect_start_x += rect_fill_x + rect_gap
    con.font = "14pt sans-serif";
    con.fillText("AWS S3 Service",
                 (rect_start_x + rect_fill_x/2),
                 (rect_start_y + rect_fill_y/2));

    add_text(con, (rect_start_x + rect_fill_x/2),
             (rect_start_y + rect_fill_y/2 + 50),
              "yellow", "18pt sans-serif", "Testmsg" );

    //con.font = "18pt sans-serif";
    //con.fillText("100%",
    //             (rect_start_x + rect_fill_x/2),
    //             (rect_start_y + rect_fill_y/2 + 50));
}


  //Draw font
  //con.fillStyle = "white"
  //con.lineWidth = "2";
  //con.font = "22pt sans-serif";
  //con.fillText("Canvas Redinging", 5, 90);

  //shadow
  //con.shadowBlur = 20;
  //con.fillStyle = "red";
  //con.shadowColor = "blue";
  //rectangle
  //con.fillRect(10, 10, 180, 180);
  //con.fillRect(210, 10, 180, 180);
  //con.fillRect(420, 10, 180, 180);


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

function widget_worker()
{
    widget_1.set_text(getRandom(34, 444));
}

widget_1 = new SingleStatWidget("canvas-row3-col1", "red");
widget_1.set_text("Testmsg");


generate_chart(false);
draw_col1_rect();
draw_col2_rect();
draw_col3_rect();
draw_fullrow_rect();

setInterval(generate_chart, (refreshInterval * 1000), true);
setInterval(worker, (refreshInterval * 1000));
setInterval(widget_worker, (refreshInterval * 2000));
