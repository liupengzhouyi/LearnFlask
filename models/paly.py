from db import db
from sqlalchemy import and_

class Play(db.Model):

    # （设置表名）
    __tablename__ = 'play'

    # （设置主键）
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255),)

    password = db.Column(db.String(255),)

# 返回一个可以用来表示对象的可打印字符串：（相当于java的toString）
    def __repr__(self):
        return '<Play 用户名：%r 密码：%r>' % (self.username, self.password)# 操作数据库

# 增
def add_object1(play):
    db.session.add(play)
    db.session.commit()
    print("添加 % r 完成" % play.__repr__)

# 查 （用到and的时候需要导入库）
def query_object(play, query_condition_u, query_condition_p):
    result = play.query.filter(and_(play.playname == query_condition_u, play.password == query_condition_p))
    print("查询 % r 完成" % play.__repr__)
    return result

# 删
def delete_object(play):
    result = play.query.filter(play.playname == '11111').all()
    db.session.delete(result)
    db.session.commit()

#改
def update_object(play):
    result = play.query.filter(play.playname == '111111').all()
