# models.py

from db import db
from sqlalchemy import and_

class Todo(db.Model):

    # （设置表名）
    __tablename__ = 'todo_list'

    # （设置主键）
    id = db.Column(db.Integer, primary_key=True,)

    do = db.Column(db.String(255),)

    year = db.Column(db.String(10),)

    month = db.Column(db.String(10),)

    day = db.Column(db.String(10),)

    done = db.Column(db.String(10),)

    # 返回一个可以用来表示对象的可打印字符串：（相当于java的toString）
    def __repr__(self):
        return '<做什么：%r 年：%r 月：%r 日： %r 是否做完： %r>' % (self.do, self.year, self.month, self.day, self.done)

# 操作数据库

# 增
def add_object(todo):
    db.session.add(todo)
    db.session.commit()
    print("添加 % r 完成" % todo.__repr__)

# 查 （用到and的时候需要导入库from sqlalchemy import and_）
def query_object(user, query_condition_u, query_condition_p):
    result = user.query.filter(and_(user.username == query_condition_u, user.password == query_condition_p))
    print("查询 % r 完成" % user.__repr__)
    return result

# 删
def delete_object(todo):
    result = todo.query.filter(todo.username == '11111').all()
    db.session.delete(result)
    db.session.commit()

#改
def update_object(todo):
    result = todo.query.filter(todo.username == '111111').all()
    result.title = 'success2018'

# 查询所有
def selectAll():
    todolist = Todo.query.all()
    return todolist