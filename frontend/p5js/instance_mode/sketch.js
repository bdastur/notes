var div1 = document.getElementById("sketch1");
var div2 = document.getElementById("sketch2");

const s = (sketch) => {
  let x = 100;
  let y = 100;

  sketch.setup = () => {
    sketch.createCanvas(200, 200);
  };

  sketch.draw = () => {
    sketch.background(0);
    sketch.fill(255);
    sketch.rect(x, y, 50, 50);
  }
}
let myp5Container1 = new p5(s, div1);

// Second way to define an instance of the p5 object.
let myp5Container2 = new p5((sketch) => {
  let x = 100;
  let y = 100;

  sketch.setup = () => {
    sketch.createCanvas(200, 200);
  };

  sketch.draw = () => {
    sketch.background(225);
    sketch.fill(0);
    sketch.rect(x, y, 50, 50);
  }
}, div2);
//let myp5Container2 = new p5(s, div2);

