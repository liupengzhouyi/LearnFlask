"""
Created on 19-10-8
@requirement:Anaconda 4.3.0 (64-bit) Python3.6
@description:
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import configparser
import os
app = Flask(__name__)

# 使用ConfigParser 首选需要初始化实例，并读取配置文件：
my_config = configparser.ConfigParser()
my_config.read('db.conf')
# 连接数据库information_collection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DEV_DATABASE_URL') or \
               "mysql+pymysql://root:Lp184126@114.116.4.196:3306/learnflaskdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
mydb = SQLAlchemy()
mydb.init_app(app)

# 用户模型
class User(mydb.Model):
  user_id = mydb.Column(mydb.Integer, primary_key=True)
  user_name = mydb.Column(mydb.String(60), nullable=False)
  user_password = mydb.Column(mydb.String(30), nullable=False)
  user_nickname = mydb.Column(mydb.String(50))
  user_email = mydb.Column(mydb.String(30), nullable=False)
  def __repr__(self):
    return '<User %r>' % self.user_name
# 获取用户列表，所有数据
@app.route('/users', methods=['GET'])
def getUsers():
  data = User.query.all()
  datas = []
  for user in data:
    datas.append({'user_id': user.user_id, 'user_name': user.user_name, 'user_nickname': user.user_nickname, 'user_email': user.user_email})
  return jsonify(data=datas)
# 添加用户数据，一条一条添加
@app.route('/user', methods=['POST'])
def addUser():
  user_name = request.form.get('user_name')
  user_password = request.form.get('user_password')
  user_nickname = request.form.get('user_nickname')
  user_email = request.form.get('user_email')
  user = User(user_name=user_name, user_password=user_password, user_nickname=user_nickname, user_email=user_email)
  try:
    mydb.session.add(user)
    mydb.session.commit()
  except:
    mydb.session.rollback()
    mydb.session.flush()
  userId = user.user_id
  if (user.user_id is None):
    result = {'msg': '添加失败'}
    return jsonify(data=result)
  data = User.query.filter_by(user_id=userId).first()
  result = {'user_id': user.user_id, 'user_name': user.user_name, 'user_nickname': user.user_nickname, 'user_email': user.user_email}
  return jsonify(data=result)

# 获取单条数据
@app.route('/user/<int:userId>', methods=['GET'])
def getUser(userId):
  user = User.query.filter_by(user_id=userId).first()
  if (user is None):
    result = {'msg': '找不到数据'}
  else:
    result = {'user_id': user.user_id, 'user_name': user.user_name, 'user_nickname': user.user_nickname, 'user_email': user.user_email}
  return jsonify(data=result)

# 修改用户数据
@app.route('/user/<int:userId>', methods=['PATCH'])
def updateUser(userId):
  user_name = request.form.get('user_name')
  user_password = request.form.get('user_password')
  user_nickname = request.form.get('user_nickname')
  user_email = request.form.get('user_email')
  try:
    user = User.query.filter_by(user_id=userId).first()
    if (user is None):
      result = {'msg': '找不到要修改的记录'}
      return jsonify(data=result)
    else:
      user.user_name = user_name
      user.user_password = user_password
      user.user_nickname = user_nickname
      user.user_email = user_email
      mydb.session.commit()
  except:
    mydb.session.rollback() # 回滚
    mydb.session.flush() # 重置
  userId = user.user_id
  data = User.query.filter_by(user_id=userId).first()
  result = {'user_id': user.user_id, 'user_name': user.user_name, 'user_password': user.user_password, 'user_nickname': user.user_nickname, 'user_email': user.user_email}
  return jsonify(data=result)

# 删除用户数据
@app.route('/user/<int:userId>', methods=['DELETE'])
def deleteUser(userId):
  User.query.filter_by(user_id=userId).delete()
  mydb.session.commit()
  return getUsers()
if __name__ == '__main__':
  app.run()

