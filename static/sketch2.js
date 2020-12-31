function setup() {
  // createCanvas(400, 400);
  createCanvas(windowWidth, windowHeight);
  noStroke();
  rectMode(CENTER);
}

function draw() {
  // background(220);
  background(235);
  fill(255,0,0,100);
  ellipse(mouseX, height/2,mouseY/2+10);
  //rect(mouseX, height/2, mouseY/2+10, mouseY/2+10);
  fill(255,255,255,100);
  var inverseX = width-mouseX;
  var inverseY = height-mouseY;
  ellipse(inverseX, height/2,(inverseY/2)+10);
  // rect(inverseX, height/2, (inverseY/2)+10, (inverseY/2)+10);
}