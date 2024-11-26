# app/tasks/__init__.py
from flask import Blueprint

# 定义蓝图
tasks_bp = Blueprint('tasks', __name__, template_folder='templates')

from . import views
