from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('webtest.html')

@app.route('/cat')
def cat():
    return render_template('cat.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()