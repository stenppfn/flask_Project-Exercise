from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号id
    account = db.Column(db.String(20), nullable=False)  # 账号非空
    pwd = db.Column(db.String(100), nullable=False)  # 密码非空
    add_time = db.Column(db.DateTime, nullable=False)  # 注册时间

    # 查询时的返回
    def __repr__(self):
        return "<User %r>" % self.account

    # 检查密码是否正确
    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)  # 编号id
    title = db.Column(db.String(100), nullable=False)  # 标题非空
    category = db.Column(db.Integer, nullable=False)  # 编号id
    user_id = db.Column(db.Integer, nullable=False)  # 作者
    logo = db.Column(db.String(100), nullable=False)  # 封面
    content = db.Column(db.Text, nullable=False)  # 内容
    add_time = db.Column(db.DateTime, default=datetime.now)  # 发布时间

    # 查询时的返回
    def __repr__(self):
        return "<Article %r>" % self.title
