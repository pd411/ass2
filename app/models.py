# coding:utf-8
import datetime
from app import db

#
class Role(db.Model):
    __tablename__ = 'roles'
    users = db.relationship('User', backref='role')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return "<Role %r>" % self.name

# 会员
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

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


# # 标签
# class Tag(db.Model):
#     __tablename__ = "tag"
#     id = db.Column(db.Integer, primary_key=True)
#     addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.utcnow())
#
#     def __repr__(self):
#         return "<Tag %r>" % self.name
#
#
# # 电影
# class Movie(db.Model):
#     __tablename__ = "movies"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255), unique=True)
#     rating = db.Column(db.Float)
#     release_time = db.Column(db.String(255))
#     overview = db.Column(db.String(255))
#     original_language = db.Column(db.String(100))
#     poster_path = db.Column(db.String(255))
#
#     def __repr__(self):
#         return "<Movie %r>" % self.title
