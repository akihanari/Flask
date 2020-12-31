function setup() {
    // createCanvas(600, 200);
    createCanvas(windowWidth, windowHeight);
    noStroke();
    fill(255);
    colorMode(HSB, 360, 100, 100, 255);
  }

  function draw() {
    background(0);

    const step = 30;

    for (let y = 0; y <= height; y += step) {
      for (let x = 0; x <= width; x += step) {
        const d = dist(x, y, mouseX, mouseY);
        const size = map(sin(d * 0.05), -1, 1, 0, 45);
        fill(map(sin(d * 0.05), -1, 1, 60, 320), 100, 100);
        // rect(x, y, size, size);
        triangle(x, y, (size - x)/2, y + 5, size, size);
      }
    }
  }
