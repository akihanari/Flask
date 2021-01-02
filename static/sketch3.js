var img;  // Declare variable 'img'.
var r = 100;
var xSpeed = 1;

var shapes = [];

function setup() {
  createCanvas(720, 400);
  img = loadImage("../assets/bg_chiheisen_green.jpg");  // Load the image
  img2 = loadImage("../assets/animal_alpaca_huacaya.png");
  shapes.push(new Shape(-r/2, height/2 + 10, true, 1));
  shapes.push(new Shape(0, height/2 + 10, false, 0));

}

function draw() {
  // Displays the image at its actual size at point (0,0)
  image(img, 0, 0);
  shapes[0].display();
  shapes[1].display();
}

function Shape(tmpX, tmpY, tmpFlag, tmpNextIndex) {
  this.x = tmpX;
  this.y = tmpY;
  this.moveFlag = tmpFlag;
  this.nextIndex = tmpNextIndex;

  this.display = function() {
    if (!this.moveFlag) {
      return;
    }

    image(img2, this.x, this.y, r, r);

    this.x -= xSpeed;

    if (this.x < width - r/2) {
      shapes[this.nextIndex].moveFlag = true;
    }

    if (this.x < -100) {
      this.x = width;
      this.moveFlag = false;
    }
  }
}