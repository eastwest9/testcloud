from flask import Flask,render_template
app = Flask(__name__)
#(flaskBlog) C:\flaskBlog>mkdir templates

@app.route("/")
def hello():
    return render_template('webtest.html')
