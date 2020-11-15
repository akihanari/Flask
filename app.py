from flask import Flask, render_template
import random
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def This_is():
        # 使うフォント，サイズ，描くテキストの設定
    ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"
    fontsize = 12
    text = "■"

    # 画像サイズ，背景色，フォントの色を設定
    canvasSize    = (300, 150)
    backgroundRGB = (255, 255, 255)
    textRGB       = (0, 0, 0)

    # 文字を描く画像の作成
    img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
    draw = PIL.ImageDraw.Draw(img)

    # 用意した画像に文字列を描く
    font = PIL.ImageFont.truetype(ttfontname, fontsize)
    textWidth, textHeight = draw.textsize(text,font=font)
    textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
    draw.text(textTopLeft, text, fill=textRGB, font=font)
    testimage = img.save("image.png")
    return render_template("about.html", testimage=testimage)

if __name__ == '__main__':
    app.run()
