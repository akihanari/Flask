function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
  rectMode(CENTER);
}

function draw() {
  background(235);
  fill(255,0,0,100);
  ellipse(mouseX, height/2,mouseY/2+10);
  fill(255,255,255,100);
  var inverseX = width-mouseX;
  var inverseY = height-mouseY;
  ellipse(inverseX, height/2,(inverseY/2)+10);

}