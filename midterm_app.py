from flask import Flask,render_template,url_for
from flask.globals import request
from flask.signals import template_rendered

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])

def login():
    return render_template("login.html")

@app.route('/registration',methods=['POST'])
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1",port = 5000,debug=True)