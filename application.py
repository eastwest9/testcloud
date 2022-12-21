from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('webtest.html')

@app.route('/cat.html')
def test():
    return render_template('cat.html')

@app.route('/test.html')
def test():
    return render_template('test.html')
