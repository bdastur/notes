var div1 = document.getElementById("sketch1");
let myp5Container1 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;
  
  let lazydot_1 = null;
  let lazydot_2 = null;

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    // sketch.fill(0, 0, 255, 105);
    sketch.noStroke();
    lazydot_1 = new LazyDot(0.01, sketch);
    lazydot_2 = new LazyDot(0.05, sketch);

  };

  sketch.drawShape = (offset) => {
    lazydot_1.moveDot(sketch.mouseX, sketch.mouseY);
    lazydot_2.moveDot(sketch.mouseX, sketch.mouseY);
  };

  sketch.draw = () => {
    sketch.drawShape(0);
  }

}, div1);


function LazyDot(easing, sketch) {
  this.sketchHandle = sketch;
  this.easing = easing;
  this.xPos = 0;
  this.yPos = 0;
  this.size = 10;

  this.sketchHandle.fill(0, 0, 255, 105);
  this.moveDot = function(mouseX, mouseY) {
    this.xPos += (mouseX -this.xPos) * this.easing;
    this.yPos += (mouseY - this.yPos) * this.easing;
    this.sketchHandle.ellipse(this.xPos, this.yPos, this.size, this.size)
  }
}


var div2 = document.getElementById("sketch2");
let myp5Container2 = new p5((sketch) => {

  let canvasWidth = 400;
  let canvasHeight = 300;
  
  let jitterbug_1 = null;
  let jitterbug_2 = null;

  let jb1x = 0;
  let jb1y = 0;

  let jb2x = 0;
  let jb2y = 0;

  sketch.setup = () => {
    sketch.createCanvas(canvasWidth, canvasHeight);
    // sketch.fill(0, 0, 255, 105);
    sketch.noStroke();
    sketch.frameRate(20);
    jitterbug_1 = new JitterBug(sketch, 400/2, 300/2, sketch.width, sketch.height, 'green', 10);
    //jitterbug_2 = new JitterBug(sketch, 400/3, 300/2, sketch.width, sketch.height, 'blue', 10);
  };

  sketch.drawShape = (offset) => {
    [jb1x, jb1y] = jitterbug_1.moveBug(jb2x, jb2y);
    //[jb2x, jb2y] = jitterbug_2.moveBug(jb1x, jb2y);
    //sketch.print("jb1x: " + jb1x + ", y: " + jb1y);
  };

  sketch.draw = () => {
    sketch.drawShape(0);
  }

}, div2);

function JitterBug(sketch, startX, startY, rangeX, rangeY, rgbColor, size) {
  this.sketchHandle = sketch;
  this.xPos = startX;
  this.yPos = startY;
  this.rangeX = rangeX;
  this.rangeY = rangeY;

  this.speed = 5;
  this.size = size;
  this.rgbColor = rgbColor;

  this.setColor = function () {
    if (this.rgbColor == "blue") {
      this.sketchHandle.fill(0, 0, 255, 80);
    } else if (this.rgbColor == "green") {
      this.sketchHandle.fill(0, 255, 0, 80);
    } else {
      this.sketchHandle.fill(0, 0, 255, 80);
    }
  }

  this.opposeOther = function(peerX, peerY) {
    let diffX = Math.abs(this.xPos - peerX);
    let diffY = Math.abs(this.yPos - peerY);
    
    if (diffX < 5 && diffY < 5) {
      let randomDirection = this.sketchHandle.random(1);
      if(randomDirection == 0) {
        this.xPos += 50;
        this.sketchHandle.print("move xdiff: " + diffX, ", ydiff: " + diffY);
      } else {
        this.yPos += 50;
        this.sketchHandle.print("move ydiff: " + diffX, ", ydiff: " + diffY);
      }
    }
    if (Math.abs(this.xPos - this.rangeX) <= 5) {
      this.sketchHandle.print("range hit xdiff: " + (this.xPos - this.rangeX));
      this.xPos -= 50;
    } else if (this.xPos <= 5) {
      this.xPos += 5;
    }
    if (Math.abs(this.yPos - this.rangeY) <= 5) {
      this.yPos -= 50;
    } else if (this.yPos <= 5) {
      this.yPos += 5;
    }
  }

  this.moveBug = function(peerX, peerY) {
    this.xPos += this.sketchHandle.random(-this.speed, this.speed);
    this.yPos += this.sketchHandle.random(-this.speed, this.speed);
    this.opposeOther(peerX, peerY);

    this.setColor();
    this.sketchHandle.ellipse(this.xPos, this.yPos, this.size, this.size);
    //this.sketchHandle.print("x: " + this.xPos + ", y: " + this.yPos);
    return [this.xPos, this.yPos];

  }
}

/****************************************************
 * Sketch 3
 */

 var div3 = document.getElementById("sketch3");
 let myp5Container3 = new p5((sketch) => {
 
   let canvasWidth = 400;
   let canvasHeight = 300;
   let bouncyBall_1 = null;
   
 
   sketch.setup = () => {
     sketch.createCanvas(canvasWidth, canvasHeight);
     sketch.noStroke();
     sketch.frameRate(30);
     sketch.background(255);
     bouncyBall_1 = new BouncyBall(sketch);
   };
 
   sketch.draw = () => {
     bouncyBall_1.move();
   }
 
 }, div3);


 function BouncyBall(sketch) {
   this.xPos = 0;
   this.yPos = 0;
   this.size = 20;
   this.sketchHandle = sketch;
   this.xDirection = 5;
   this.yDirection = 2;
   this.sketchHandle.fill(0, 0, 255, 80);

   let rBorder = 0;
   let lBorder = 0;
   let upBorder = 0;
   let downBorder = 0;

   this.move = function() {
     rBorder = Math.abs(this.sketchHandle.width - this.xPos);
     lBorder = Math.abs(this.xPos - 0);
     upBorder = Math.abs(this.yPos - 0);
     downBorder = Math.abs(this.sketchHandle.height - this.yPos);


     if (rBorder < 5) {
       //change xDirection.
       this.xDirection = -1 * this.sketchHandle.random(6);
     }

     if (lBorder < 5 ) {
       this.xDirection = this.sketchHandle.random(5);
     }

     if (upBorder < 5) {
       this.yDirection = this.sketchHandle.random(6);
       this.sketchHandle.print("upborder: " + upBorder + ", y: " + this.yPos);

     }

     if (downBorder < 5) {
       this.yDirection = -1 * this.sketchHandle.random(5);
       this.sketchHandle.print("downborder: " + downBorder + ", y: " + this.yPos);
     }
     this.xPos += this.xDirection;
     this.yPos += this.yDirection;

     sketch.background(255);
     this.sketchHandle.beginShape();
     this.sketchHandle.ellipse(this.xPos, 
                               this.yPos, this.size, this.size);
     this.sketchHandle.ellipse((this.xPos - this.size), 
                               (this.yPos - this.size), 
                               this.size, this.size);
     this.sketchHandle.endShape();
   }
 }


 /****************************************************
 * Sketch 4 - Vector
 */

  var div4 = document.getElementById("sketch4");
  let myp5Container4 = new p5((sketch) => {
  
    let canvasWidth = 400;
    let canvasHeight = 300;
    let v1;
  
    sketch.setup = () => {
      sketch.createCanvas(canvasWidth, canvasHeight);
      sketch.stroke(255,0, 255);
      sketch.strokeWeight(2);
      v1 = sketch.createVector(sketch.width/2, sketch.height/2, 50);
    };
  
    sketch.draw = () => {
      //sketch.background(255);
      sketch.line(v1.x, v1.y, sketch.mouseX, sketch.mouseY);
    }
  
  }, div4);
