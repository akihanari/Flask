
    // let canvas;
    setup = () => {
  createCanvas(202, 202), background(210);
//   canvas.parent("P5canvas");
  var r = [0, 1, 2, 3],
    a = [];
  for (j = 0; j < 64; j++) a.push(random(r));
  for (m = 0; m < 8; m++) {
    for (k = 0; k < 8; k++) 0 == a[k] ? fill(random(255), 200, 200) : fill("#ededed"), rect(1 + 25 * k, 1 + 25 * m, 25, 25);
    a.splice(0, 8)
  }
}, draw = () => {};
