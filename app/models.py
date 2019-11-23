# coding:utf-8
import datetime
from app import db


# 会员
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱

    # is_authenticated 方法有一个具有迷惑性的名称。
    # 一般而言，这个方法应该只返回 True，
    # 除非表示用户的对象因为某些原因不允许被认证
    @property
    def is_authenticated(self):
        return True

    # is_active 方法应该返回 True，除非是用户是无效的，
    # 比如因为他们的账号是被禁止
    @property
    def is_active(self):
        return True

    # is_anonymous 方法应该返回 True，
    # 如果是匿名的用户不允许登录系统。
    @property
    def is_anonymous(self):
        return False

    # get_id 方法应该返回一个用户唯一的标识符，以 unicode 格式。
    # 我们使用数据库生成的唯一的 id。
    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlogs"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  # 所属会员
    ip = db.Column(db.String(100))  # ip地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())  # 登陆时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


class Movie:
    def __init__(self, title, language, overview, release_time, \
                 runtime, vote_count, director, star, writer):
        self.title = title
        self.language = language
        self.overview = overview
        self.release_time = release_time
        self.runtime = runtime
        self.vote_count = vote_count
        self.director = director
        self.star = star
        self.writer = writer