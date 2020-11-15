from flask import Flask, render_template
import random
from PIL import Image, ImageFilter
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def This_is():
    font = ImageFont.truetype('/Library/Fonts/Arial Bold.ttf', 48)
    draw.multiline_text((0, 0), 'Pillow sample', fill=(0, 0, 0), font=font)
    testimage = im.save('data/dst/pillow_iamge_draw.jpg', quality=95)
    return render_template("about.html", testimage=testimage)

if __name__ == '__main__':
    app.run()
