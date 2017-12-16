
/*
 * SingleStatsWidget Class.
 */
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

    // Initialize msgs
    this.msgs = [];
    this.msgcount = 0;

    this.div_id = div_id;
    this.widget_color = widget_color;

    /* Draw the widget */
    this.drawing = document.getElementById(this.div_id);
    this.con = this.drawing.getContext("2d");

    this.con.shadowBlur = 10;
    this.con.fillStyle = this.widget_color;
    this.con.shadowColor = "black";
    this.con.fillRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);

    console.log("SingleStatWidget Initalized.", this.div_id, ": color",
                this.widget_color);
}

SingleStatWidget.prototype.redraw_widget = function(widget_color)
{
    console.log("Draw Widget invoked.")
    if (widget_color != undefined) {
        this.con.fillStyle = this.widget_color
    } else {
        this.con.fillStyle = this.widget_color;
    }

    this.con.shadowBlur = 10;
    this.con.shadowColor = "black"
    this.con.fillRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);
}


SingleStatWidget.prototype.set_text = function(msg, id, fontstyle)
{
    /* Overwrite text */
    this.con.clearRect(this.pos_x, this.pos_y, this.fill_x, this.fill_y);
    this.redraw_widget();

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
