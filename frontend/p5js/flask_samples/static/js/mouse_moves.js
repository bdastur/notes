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
  };

  sketch.drawShape = (offset) => {
    sketch.ellipse(sketch.mouseX, sketch.mouseY, 9, 9);
  }

  sketch.draw = () => {
    sketch.fill(0, 0, 255, 105);
    sketch.background(255);  // Setting background will not leave a trail
    // Note here we call a helper function to draw the actual shape.
    sketch.drawShape(0);
  };

}, div1);

/*
 * p5.js shapes.
 */
var div2 = document.getElementById("sketch2");
let myp5Container2 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.fill(0, 0, 255, 105);
    sketch.noStroke();
  };

  sketch.drawShape = (offset) => {
    var defaultSize = 15;
    var size = sketch.dist(sketch.mouseX, sketch.mouseY, 
                             sketch.pmouseX, sketch.pmouseY);
    if (size < defaultSize) {
      size = defaultSize;
    }
    sketch.ellipse(sketch.mouseX, sketch.mouseY, size, size);
  };

  sketch.draw = () => {
    sketch.drawShape(0);

  }

}, div2);



var div3 = document.getElementById("sketch3");
let myp5Container3 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;
  let easing = 0.05;
  let x = 0;
  let y = 0;

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.fill(0, 0, 255, 105);
    sketch.noStroke();
  };

  sketch.drawShape = (offset) => {
    if (sketch.mouseIsPressed) {
      if (sketch.mouseButton == sketch.LEFT) {
        sketch.fill(255, 0, 0, 105);
      } else if (sketch.mouseButton == sketch.RIGHT) {
        sketch.fill(0, 255, 0, 105);
      } else if (sketch.mouseButton == sketch.CENTER) {
        sketch.fill(0, 0, 0, 105);
      }
    } else {
      sketch.fill(0, 0, 255, 105);
    }

    var targetX = sketch.mouseX;
    var targetY = sketch.mouseY;

    x += (targetX - x) * easing;
    y += (targetY - y) * easing;

    sketch.ellipse(x, y, 12, 12);
    //sketch.print(targetX + " : " + x);
  };

  // Create a function to draw a custom shape.
  // This shows how offset can be used to ensure the shape follows 
  // the mouse movements.
  sketch.drawArrow = () => {
    var startX = sketch.mouseX;
    var startY = sketch.mouseY;
    sketch.stroke(2);
    sketch.line(startX, startY, startX + 20, startY - 10);
    sketch.line(startX, startY, startX + 90, startY);
    sketch.line(startX, startY, startX + 20, startY + 10);

  }

  sketch.draw = () => {
    sketch.drawShape(0);
    sketch.drawArrow();
  }

}, div3);


var div4 = document.getElementById("sketch4");
let myp5Container4 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;
  let x = 40;
  let y = 80;
  let toggle = false;

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.textSize(24);
    sketch.textAlign(sketch.CENTER);
    sketch.stroke(255);
    sketch.fill(255);
    sketch.background(0);
  };

  sketch.keyReleased = () => {
    sketch.print("Key Release Key: " + sketch.key + ", x, y: " + x + " , " + y);
    toggle = false;
  }

  sketch.draw = () => {
    
    if (sketch.keyIsPressed && !toggle) {
      if (sketch.keyCode != sketch.SHIFT && 
          sketch.keyCode != sketch.BACKSPACE && sketch.keyCode != sketch.ENTER) { 
        sketch.text(sketch.key, x, y);
      }
      sketch.print("Key: " + sketch.key + ", x, y: " + x + " , " + y);
      x = x + 14;
      if (sketch.width -x < 10) {
        x = 10;
        y = y + 22;
      }
      toggle = true;
    }
  }

}, div4);