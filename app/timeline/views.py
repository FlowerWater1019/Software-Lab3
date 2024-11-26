# app/timeline/views.py
from flask import render_template, request, redirect, url_for, flash
from app.extensions import db
from . import timeline_bp
from app.models import Task
from datetime import datetime

@timeline_bp.route('/timeline')
def sort_timeline():
    tasks = Task.query.order_by(Task.deadline.asc()).all()
    return render_template('sort_timeline.html', tasks=tasks)
