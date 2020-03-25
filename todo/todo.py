# login.py
from flask import Blueprint, render_template, request

from models.todo import Todo, add_object, selectAll

todo_blueprint = Blueprint(
    'todo',
    __name__,
    url_prefix='/todo',
    template_folder='todoTemplate'
)

@todo_blueprint.route('/')
def index():
    return render_template('todoIndex.html')

@todo_blueprint.route('/add')
def add():
    return render_template('addtodo.html')


@todo_blueprint.route('/getDate', methods=['POST', 'GET'])
def getDate():
    todoname = request.form.get('todoname')
    year = request.form.get('year')
    month = request.form.get('month')
    day = request.form.get('day')
    todo = Todo()
    todo.done = '0'
    todo.do = todoname
    todo.year = year
    todo.month = month
    todo.day = day
    print("添加 % r 完成" % todo.__repr__)
    add_object(todo)
    return render_template('todoIndex.html')

@todo_blueprint.route('/getAll', methods=['POST', 'GET'])
def getAll():
    todolist = selectAll()
    longth = len(todolist)
    return render_template('todoshowList.html', todolist=todolist, longth=longth)
