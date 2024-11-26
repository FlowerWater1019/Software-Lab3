# app/timeline/__init__.py
from flask import Blueprint

timeline_bp = Blueprint('timeline', __name__, template_folder='templates')

from . import views
