## 文档介绍：
app是项目文档，项目文档分为两个部分
- admin: 做api的内容
- home: 前端的内容

## mysql的修改：
在app/__init__.py中:

``
    homeApp.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Unsw1995@localhost:3306/movie"
``
中间root:Unsw1995 （username:password）
mysql的命令：

``
    mysql -uroot -p
``

## api编写部分：
在app/admin/views.py

## 数据库的migrate:
在terminal中先切入当前目录输入python
在输入：
``
    from app import db
    db.create_all()
``
