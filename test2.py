from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [[random.randrange(4) for i in range(16)] for j in range(16)]
    return render_template("index.html", numbers = numbers)

@app.route('/about')
def This_is():
    return 'This is Flask'

if __name__ == '__main__':
    app.run()
