var div1 = document.getElementById("sketch1");
let myp5Container1 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;
  
  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    sketch.background(204);
    sketch.stroke(140);
  };

  sketch.drawGrid = () => {
    sketch.stroke(230);
    for (let i = 10; i < sketch.width; i += 10) {
      sketch.line(i, 0, i, 300);
    }

    for (let i=10; i < sketch.height; i+= 10) {
      sketch.line(0, i, 400, i);
    }
  }

  sketch.draw = () => {
    sketch.drawGrid();

    sketch.stroke(140);
    sketch.rect(100, 100, 30, 30);
    sketch.translate(-50, 30);
    sketch.rect(100, 100, 30, 30);
    sketch.stroke(0);
    //sketch.line(33, 2, 33, 200);
  }

}, div1);

