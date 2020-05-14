/*
 * D3 Practice
*/
console.log("D3 Practice JS");

d3.select("p").style("color", "green");
d3.select(".red-paragraph").style("color", "red");
d3.select("#para3").style("color", "blue");

d3.selectAll("p").style("color", "red");

d3.select("tr").selectAll("td").style("background-color", "yellow");


var tr_objects = d3.selectAll("tr");
console.dir(tr_objects);

tr_objects._groups.forEach(obj => {
    console.log("obj: " + obj);
});


d3.select("#para5").text("A new text")

// var data = [1100, 2010, 3100];
// var paragraph = d3.select("body")
//                 .selectAll("p")
//                 .data(data)
//                 .text(function (d, i) {
//                     console.log("d: " + d);
//                     console.log("i: " + i);
//                     console.log("this: " + this);

//                     return d;
//                 });


var divobj = d3.selectAll("div");
divobj.on('mouseover', function() {
    divobj.style('background-color', 'orange');
    divobj.text('On mouse over');
}).on('click', function() {
    divobj.text('Clicked!');
}).on('mouseout', function() {
    divobj.style('background-color', 'steelblue');
    divobj.text('Onmouse out');
});

/*
 * D3 is data driven. The data() function is used to join the specified
 * array of data to the selected DDM elements.
 * You can pass two types of values to the data() function. An array of
 * values or a function of data.
 */

var myData = ["Hello World!", "Hello Data", "Hello D3",
              "101", "201",
              "301", "401", "501"];

var p = d3.select("body")
    .selectAll("p")
    .data(myData)
    .enter()
    .append("p")
    .text(function (d, idx) {
        console.log("Text function: " + d + ", index: " + idx);
        return d;
    });

d3.select("body")
    .select("p")
    .datum(100000)
    .text(function (d, i) {
        return d;
    });



/*
 * Handliing CSV files.
 */
d3_body_obj = d3.select("body");

d3.csv("/data/jira_samples.csv", function(d) {
    return {
        id: d.issue,
        summary: d.summary,
        priority: d.priority,
        status: d.status,
        storypoints: d.storypoints
    };
}).then(function(data) {
    for (let i = 0; i < data.length; i++) {
        console.log("Issue: " + data[i].id + ", Summary: " + data[i].summary);
        para_msg = "Issue: " + data[i].id + ", Summary: " + data[i].summary;
        d3_body_obj.append("p").text(para_msg);
    }
});



var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'My First dataset',
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45]
        }]
    },

    // Configuration options go here
    options: {}
});

var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["jan", "feb", "march", "april"],
        datasets: [{
            label: 'Weekly rise',
            backgroundColor: 'rgba(255, 99, 132, 0.75)',
            borderColor: 'rgba(255, 99, 132. 1.0)',
            data: [10, 34, 43, 43 ]
        }]
    },

    // Configuration options go here
    options: {}
});


var ctx = document.getElementById('myChart');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});