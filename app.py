from flask import Flask, render_template
import random
from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def num_to_english(x):
    """ 数字の英語文字列を返す """
    assert 0 <= x <= 9, "Input int x (0 <= x <= 9)"
    return ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")[x]


def make_image(idx, font_name):
    W = 28
    H = 28
    """ フォントを指定して 0-9 の画像ファイルを作る """
    fnt = ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF".format(font_name), 25)
    for i in range(10):
        back_image = Image.new("RGBA", (W, H), (255, 255, 255, 0))
        txt_image = Image.new('RGBA', (W, H), (0, 0, 0, 255))
        draw = ImageDraw.Draw(txt_image)

        tw, th = fnt.getsize(str(i))  # フォントを指定した時のサイズ（位置計算に使用）
        draw.text(((W - tw) / 2, (H - th) / 2), str(i), font=fnt, fill=(255, 255, 255, 255))
        file_name = "testimage.png".format(num_to_english(i), idx)
        out = Image.alpha_composite(back_image, txt_image)
        out.save("images/" + file_name)


def main():
    # ttfファイルのみ取得する
    rp = re.compile(".*ttf")
    font_list = [fnt for fnt in os.listdir("C:/Windows/Fonts") if rp.match(fnt)]

    for idx, font_name in enumerate(font_list):
        make_image(idx, font_name)

if __name__ == '__main__':
    app.run()
