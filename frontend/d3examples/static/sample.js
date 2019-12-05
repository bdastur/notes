alert(d3.select("h1").text());
console.log("Test 4")

divobj = d3.select("div.myd3")
divobj.text("This text was created from d3.js")

d3.select("div.myd3").append("span").text("This is a test")


divobj = d3.select("div.myd32")
divobj.html("Hello Div32<h4>tthis is a ttest</h4>")
divobj.attr("style", "color: red");



d3.select("#list").selectAll("li")
  .data([10, 20, 30, 40, 50])
  .text(function(d) { return "This is pre-existing element and the value is " + d; })
  .enter()
  .append("li")
  .text(function(d)
    { return "This is dynamically created element and the value is " + d; });


console.log("Here 4")

// SVG Creation

var svg = d3.select("#svgcontainer")
            .append("svg")
            .attr("width", 300)
            .attr("height", 300);
         //Create and append rectangle element
         svg.append("rect")
            .attr("x", 20)
            .attr("y", 20)
            .attr("width", 200)
            .attr("height", 100)
            .attr("fill", "green");




var svgContainer = d3.select("#svgcontainer")
var svg = svgContainer.append("svg")
  .attr("width", 300)
  .attr("height", 300)
svg.append("rect")
  .attr("x", 20)
  .attr("y", 20)
  .attr("width", 200)
  .attr("height", 100)
  .attr("fill", "red");



// SVG Transformations.

var width = 300;
var height = 300;
var svg = d3.select("#svggroup2")
   .append("svg")
   .attr("width", width)
   .attr("height", height);

var group = svg.append("g")
   .attr("transform", "translate(60, 60) rotate(30)");

var rect = group.append("rect")
   .attr("x", 20)
   .attr("y", 20)
   .attr("width", 60)
   .attr("height", 30)
   .attr("fill", "black")

var circle = group
   .append("circle")
   .attr("cx", 0)
   .attr("cy", 0)
   .attr("r", 50)
   .attr("fill", "red")
   .text("Text in circle")


// Tansitions.


