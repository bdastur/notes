/*
 * SingleStatGridbox Class.
 * Represents single stat values represented in the gridster grid.
 */
var SingleStatGridbox = function(id,
                                 metric_name,
                                 metric_value,
                                 thresholds)
{
     this.id = "#" + id;
     this.metric_name = metric_name;
     this.metric_value = metric_value;

     if (thresholds == undefined) {
         this.thresholds = {
             'OK': 90,
             'WARNING': 80,
             'FAIL': 70
         };
     } else {
         this.thresholds = thresholds;
     }

     //threshold colors.
     this.threshold_colors = {
         'OK': 'green',
         'WARNING': 'yellow',
         'FAIL': 'red'
     };

     msg = "<h3>" + this.metric_name + "</h3>" + "\n";
     msg += "<br>" + "<h5>" + this.metric_value + "<h5>";
     $(this.id).html(msg);

     console.log("SingleStatGridbox Initialized!");
 };


 SingleStatGridbox.prototype.check_thresholds = function(metric_value) {
     var status = 'OK';
     var diff = 0;
     for (var threshold in this.thresholds) {
        console.log("Threshold: ", threshold, " , \
        value: ", this.thresholds[threshold]);
        if (metric_value < this.thresholds[threshold]) {
            if (diff == 0) {
                status = threshold;
                diff = this.thresholds[threshold] - metric_value;
            } else if ((this.thresholds[threshold] - metric_value) < diff) {
                status = threshold;
            }
        }
     }
     return status;
 };


SingleStatGridbox.prototype.update_message = function(metric_value,
                                                      lastupdated_string)
{
    old_metric_value = this.metric_value;
    this.metric_value = metric_value;

    status = this.check_thresholds(metric_value);

    diff = metric_value - old_metric_value;
    if (diff < 0) {
        msg_change = "Value Down " + diff + " from previous";
    } else {
        msg_change = "Value Up " + diff + " from previous";
    }

    msg = "<h3>" + this.metric_name + "</h3>" + "\n";
    msg += "<br>" + "<h5>" + this.metric_value + "<h5>";
    msg += "<br>" + msg_change;
    msg += "<br>" + "Status: " + status;

    if (lastupdated_string != undefined) {
        msg += "<p></p><p></p><p></p>" + "<font size=\"3\" color=\"black\">" +
        "</font>Last Updated: " + lastupdated_string;
    }


    console.log("msg: ", msg);
    $(this.id).html(msg);
    this.update_gridbox_color(status);
};

SingleStatGridbox.prototype.update_gridbox_color = function (status) {
    $(this.id).css({backgroundColor: this.threshold_colors[status]});
};
