
var refreshInterval = 5;
var myChart;



function widget_worker(){
    widget_11.set_text(getRandom(34, 444), 0);
    widget_12.set_text(getRandom(64, 1444), 0);
    widget_13.set_text(getRandom(234, 4444), 0);
}


widget_11 = new SingleStatWidget("can-row1col1", "red");
widget_11.set_text("Testmsg", 0);

widget_12 = new SingleStatWidget("can-row1col2", "green");
widget_12.set_text("Testmsg", 0);

widget_13 = new SingleStatWidget("can-row1col3", "red");
widget_13.set_text("Testmsg", 0);


/*
var gridster;

$(function() {
    gridster = $(".gridster > ul").gridster({
        widget_margins: [10, 10],
        widget_base_dimensions: [140, 140],
        min_cols: 6
    }).data('gridster');
    console.log("GRIDSTER Initialize");
});
*/

//setInterval(widget_worker, (refreshInterval * 1000));
