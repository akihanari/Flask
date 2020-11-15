from flask import Flask, render_template
import random
from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def This_is():
    testimage_path = 'images/testimage.png'
    testimage = Image.open(testimage_path).copy()

    position = ("50", "50")
    font = ImageFont.truetype("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap", 12)
    draw = ImageDraw.Draw(testimage)

    draw.text(position, "■", "000000", font=font)

    testimage = img.save(testimage_path)
    return render_template("about.html", testimage=testimage)

if __name__ == '__main__':
    app.run()
