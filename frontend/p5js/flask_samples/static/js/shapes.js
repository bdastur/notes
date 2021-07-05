var div1 = document.getElementById("sketch1");

function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

/*
 * p5.js : point
 */
let myp5Container1 = new p5((sketch) => {
  let canvasWidth = 200;
  let canvasHeight = 150;


  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.frameRate(30);
  };

  sketch.draw = () => {
    sketch.background(0);
    sketch.stroke(255);
    strength = 255;
    for (let x = 10; x < canvasWidth; x += 10) {
      sketch.stroke(strength);
      for (let y = 10; y < canvasHeight; y += 10) {
        sketch.point(x, y);
      }
      strength -= 5;
    }

  }
}, div1);

/*
 * p5.js shapes.
 */
var div2 = document.getElementById("sketch2");

let myp5Container2 = new p5((sketch) => {
  let canvasWidth = 600;
  let canvasHeight = 400;
  let radian = 1


  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.frameRate(15);
    sketch.stroke(0);
    sketch.strokeWeight(5);
    sketch.strokeCap(sketch.ROUND);
    sketch.fill(255, 0, 0);
  };

  sketch.draw = () => {
    sketch.background(204);

    //line.
    sketch.line(4, 10, 190, 50);

    //triangle.
    sketch.fill(255, 0, 0, 50);
    sketch.triangle(90, 40, 200, 140, 40, 209);

    //Quadrilateral.
    sketch.fill(255, 0, 0, 100);
    sketch.quad(40, 50, 240, 67, 29, 43, 130, 260);

    //rectangle
    sketch.fill(0, 0, 255, 150);
    sketch.rect(150, 150, 100, 100);

    //ellipse
    sketch.fill(255, 0, 0, 105);
    sketch.ellipse(250, 200, 80, 80);

    //arc.
    sketch.arc(50, 300, 90, 90, 0, sketch.HALF_PI);
    sketch.arc(150, 300, 90, 90, 0, sketch.PI);
    sketch.arc(250, 300, 90, 90, 0, sketch.HALF_PI + sketch.PI);

    sketch.noFill(); //No fill for these shapes.
    sketch.strokeWeight(1); //Change the stroke weight for these shapes.
    sketch.arc(350, 300, 90, 90, 0, 10);
    sketch.arc(450, 300, 90, 90, 0, 50);

    sketch.arc(550, 300, 90, 90, sketch.radians(0), sketch.radians(radian));
    radian += 1

  }
}, div2);
