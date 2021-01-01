from flask import Flask, render_template
import random
from PIL import Image, ImageDraw, ImageFont
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db_uri = 'sqlite:///test.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# db = SQLAlchemy(app)

# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     pub_date = db.Column(db.DateTime, nullable=False,
#                                 default=datetime.utcnow)
#     name = db.Column(db.Text())
#     article = db.Column(db.Text())
#     thread_id = db.Column(db.Integer, db.ForeignKey('thread.id'), nullable=False)

#     def __init__(self, pub_date, name, article, thread_id):
#         self.pub_date = pub_date
#         self.name = name
#         self.article = article
#         self.thread_id = thread_id

# class Thread(db.Model):
#     #__tablename__ = "threads"
#     id = db.Column(db.Integer, primary_key=True)
#     threadname = db.Column(db.String(80), unique=True)
#     #threadname = db.Column(db.Text(80), unique=True)
#     articles = db.relationship('Article', backref='thread', lazy=True)

#     def __init__(self, threadname, articles=[]):
#         self.threadname = threadname
#         self.articles = articles

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/pixelart")
def pixel():
    numbers = [[random.randrange(4) for i in range(8)] for j in range(8)]
    return render_template("pixelart.html", numbers = numbers)

@app.route('/p5js')
def p5js():
    return render_template("p5js.html")

@app.route('/p5js1')
def p5js1():
    return render_template("p5js1.html")

@app.route('/p5js2')
def p5js2():
    return render_template("p5js2.html")

# @app.route("/bbs")
# def bbs():
#     threads = Thread.query.all()
#     # print("\n---------------------------------------------")
#     # print(text)
#     # print(type(text))
#     # print("---------------------------------------------\n")
#     return render_template("index.html", threads=threads)

# @app.route("/thread", methods=["POST"])
# def thread():
#     thread_get = request.form["thread"]
#     threads = Thread.query.all()
#     #articles = Article.query.all()
#     thread_list = []
#     threads = Thread.query.all()
#     for th in threads:
#         thread_list.append(th.threadname)
#         #print("----" + th.threadname + "----")
#     if thread_get in thread_list:
#         thread = Thread.query.filter_by(threadname=thread_get).first()
#         articles = Article.query.filter_by(thread_id=thread.id).all()
#         return render_template("thread.html",
#                                 articles=articles,
#                                 thread=thread_get)
#     else:
#         thread_new = Thread(thread_get)
#         db.session.add(thread_new)
#         db.session.commit()
#         articles = Article.query.filter_by(thread_id=thread_new.id).all()
#         return render_template("thread.html",
#                                 articles=articles,
#                                 thread=thread_get)

# @app.route("/result", methods=["POST"])
# def result():
#     date = datetime.now()
#     article = request.form["article"]
#     name = request.form["name"]
#     thread = request.form["thread"]
#     #print(article)
#     #print(name)
#     #print("------------------------------------------------------------")
#     #print(thread)
#     #print("------------------------------------------------------------")
#     thread = Thread.query.filter_by(threadname=thread).first()
#     #print(thread)
#     #print("------------------------------------------------------------")
#     admin = Article(pub_date=date, name=name, article=article, thread_id=thread.id)
#     db.session.add(admin)
#     db.session.commit()
#     return render_template("bbs_result.html", article=article, name=name, now=date)
# @app.route('/about')
# def num_to_english(x):
#    """ 数字の英語文字列を返す """
#    assert 0 <= x <= 9, "Input int x (0 <= x <= 9)"
#     return ("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")[x]


# def make_image(idx, font_name):
#    W = 28
#    H = 28
#    """ フォントを指定して 0-9 の画像ファイルを作る """
#    fnt = ImageFont.truetype("C:/Windows/Fonts/BAUHS93.TTF".format(font_name), 25)
#    for i in range(10):
#        back_image = Image.new("RGBA", (W, H), (255, 255, 255, 0))
#        txt_image = Image.new('RGBA', (W, H), (0, 0, 0, 255))
#        draw = ImageDraw.Draw(txt_image)

#        tw, th = fnt.getsize(str(i))  # フォントを指定した時のサイズ（位置計算に使用）
#        draw.text(((W - tw) / 2, (H - th) / 2), str(i), font=fnt, fill=(255, 255, 255, 255))
#        file_name = "testimage.png".format(num_to_english(i), idx)
#        out = Image.alpha_composite(back_image, txt_image)
#        out.save("images/" + file_name)


# def main():
    # ttfファイルのみ取得する
#    rp = re.compile(".*ttf")
#    font_list = [fnt for fnt in os.listdir("C:/Windows/Fonts") if rp.match(fnt)]

#    for idx, font_name in enumerate(font_list):
#        make_image(idx, font_name)

if __name__ == '__main__':
    app.run()
