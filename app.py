from flask import Flask, render_template
import random
from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def This_is(font_path="images/font.ttf", dst_path="dst.png", text="■", font_size=32, font_color="white"):
    font = ImageFont.truetype(font_path, font_size)
    # get fontsize

    tmp = Image.new('RGBA', (1, 1), (0, 0, 0, 0)) # dummy for get text_size

    tmp_d = ImageDraw.Draw(tmp)
    text_size = tmp_d.textsize(text, font)
    # draw text

    img = Image.new('RGBA', text_size, (0, 0, 0, 0)) # background: transparent

    img_d = ImageDraw.Draw(img)
    img_d.text((0, 0), text, fill=font_color, font=font)
    testimage = img.save(dst_path)
    return render_template("about.html", testimage=testimage)

if __name__ == '__main__':
    app.run()
