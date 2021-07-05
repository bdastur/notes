var div1 = document.getElementById("sketch1");

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

/*
 * p5.js : point
 */
let myp5Container1 = new p5((sketch) => {
  let canvasWidth = 400;
  let canvasHeight = 300;


  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.frameRate(30);
  };

  sketch.drawShape = (offset) => {
    sketch.beginShape();
    let start = offset;
    sketch.vertex(80, 80);
    sketch.vertex(40, 40);
    sketch.vertex(90, 5);
    sketch.vertex(85, 45);
    sketch.vertex(220, 50);
    sketch.vertex(220, 70);
    sketch.vertex(80, 70);
    sketch.endShape(sketch.CLOSE); //endShape() with CLOSE will join the
                                  // last vertex to the first.
  }

  sketch.draw = () => {
    sketch.strokeWeight(2);
    sketch.fill(0, 0, 255, 105);
    sketch.background(204);
    // Note here we call a helper function to draw the actual shape.
    sketch.drawShape(0);

  }
}, div1);

/*
 * p5.js shapes.
 */
var div2 = document.getElementById("sketch2");

let myp5Container2 = new p5((sketch) => {
  let canvasWidth = 400;
  let canvasHeight = 200;
  

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.fill(255);
    sketch.stroke(55);
    sketch.frameRate(1);
  };

  sketch.draw = () => {
    sketch.background(0);
    for (var y = 20; y < sketch.height-20; y += 10) {
      for (var x = 20; x < sketch.width-20; x += 10) {
        sketch.ellipse(x, y, 4, 4);
        sketch.line(x, y, sketch.width/2, sketch.height/2);
      }
    }
    // draw() API runs in a loop. Here we can see the frame count in
    // the console.
    sketch.print(sketch.frameCount);
    

  }
}, div2);
