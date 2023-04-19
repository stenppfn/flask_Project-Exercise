from datetime import datetime
import os

from flask import Flask, render_template, redirect, url_for, flash, session, Response, request
from .forms import LoginForm, RegisterForm, ArticleAddForm, ArticleEditForm
from .models import User, Article
from app.home import home

from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from functools import wraps


@home.route('/')
def hello():
    return "hello world"


# 登录装饰器
def user_login_req(f):
    @wraps(f)
    def login_req(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return login_req


# login 用户登录
@home.route("/login/", methods=["GET", "POST"])  # 用户登录
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        session["user"] = data["account"]
        flash("登录成功", "ok")
        return redirect("/art/list/1/")
    # 返回渲染模板
    return render_template("login.html", title="登录", form=form)



# register 用户注册
@home.route("/register/", methods=["GET", "POST"])  # 用户注册
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        # 保存数据
        user = User(
            account=data["account"],
            # 对于pwd进行加密
            pwd=generate_password_hash(data["pwd"]),
            add_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        db.session.add(user)
        db.session.commit()
        # 定义一个会话的闪现
        flash("注册成功, 请登录", "ok")
        return redirect("/login/")
    return render_template("register.html", title="注册", form=form)

# 验证码
@home.route("/captcha/", methods=["GET"])
def captcha():
    from ..utils import captcha
    c = captcha.Captcha()
    info = c.create_captcha()
    current_path = os.path.abspath(os.path.dirname(__file__))
    parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
    print(current_path)
    path = r"../static/captch/"
    image = path + info["image_name"]


    print(image)
    #临时修改
    image = r'D:\PythonSpace\flask_Project-Exercise\app\static\captcha\0f7ce0137ac742c1a59f3a14bbbc38ca.jpg'
    with open(image, 'rb') as f:
        image = f.read()
    session['captcha'] = info["captcha"]
    # print(session['captcha'])
    return Response(image, mimetype="jpeg")

