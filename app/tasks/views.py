# app/tasks/views.py
from flask import render_template, request, redirect, url_for, flash
from . import tasks_bp 
from app.extensions import db
from app.models import Category, Task
from datetime import datetime

@tasks_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@tasks_bp.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        deadline = request.form['deadline']
        details = request.form['details']
        category_id = request.form['category_id']
        need_reminder = bool(request.form['need_reminder'])
        ddl_delta = request.form['ddl_delta']
        
        task = Task(name=name, deadline=datetime.strptime(deadline, '%Y-%m-%dT%H:%M'), 
                    details=details, category_id=category_id, 
                    need_reminder=need_reminder, ddl_delta=ddl_delta)
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!')
        return redirect(url_for('tasks.index'))
    categories = Category.query.all()
    return render_template('add_task.html', categories=categories)


@tasks_bp.route('/task/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('tasks.index'))


@tasks_bp.route('/task/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    categories = Category.query.all()
    if request.method == 'POST':
        task.name = request.form['name']
        task.deadline = datetime.strptime(request.form['deadline'], '%Y-%m-%dT%H:%M')
        task.details = request.form['details']
        task.category_id = request.form['category_id']
        task.need_reminder = bool(request.form['need_reminder'])
        task.ddl_delta = request.form['ddl_delta']
        
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('tasks.index'))
    return render_template('edit_task.html', task=task, categories=categories)
