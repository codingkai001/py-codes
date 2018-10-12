import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/index', methods=["get", "POST"])
def home():
    user = request.form.get('user')
    psw = request.form.get('password')
    sex = request.form.get('sex')
    print(user, psw, sex)
    return "<h1>已获取表单</h1>"


if __name__ == '__main__':
    app.run()
