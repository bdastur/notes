
var refreshInterval = 5;

var gridster = null;
$(document).ready(function () {
    gridster = $(".gridster ul").gridster({
        widget_base_dimensions: ['auto', 140],
        autogenerate_stylesheet: true,
        min_cols: 1,
        max_cols: 6,
        widget_margins: [5, 5],
        resize: {
            enabled: true
        }
    }).data('gridster');
    $('.gridster  ul').css({'padding': '0'});
});

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
$('.gridster #box21').css({backgroundColor: 'blue'});

/*
for (var property in mystyles) {
    console.log("Property: ", property, "  Value: ", mystyles[property]);
}
*/

setInterval(regenerate_chart, (refreshInterval * 1000));
