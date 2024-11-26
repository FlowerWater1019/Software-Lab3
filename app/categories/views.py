# app/categories/views.py
from flask import render_template, request, redirect, url_for, flash
from app.extensions import db
from . import categories_bp
from app.models import Category, Task
from datetime import datetime

@categories_bp.route('/category')
def show_category():
    categories = Category.query.all()
    return render_template('show_category.html', categories=categories)

@categories_bp.route('/category/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['category_name']
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!')
        return redirect(url_for('categories.show_category'))
    return render_template('add_category.html')

@categories_bp.route('/category/tasks/<int:category_id>')
def category_tasks(category_id):
    category = Category.query.get(category_id)
    tasks = category.tasks
    return render_template('category_tasks.html', category=category, tasks=tasks)

@categories_bp.route('/category/delete', methods=['POST', 'GET'])
def delete_category():
    categories = Category.query.all()
    if request.method == 'POST':
        category_id = request.form['category_id']
        category = Category.query.get(category_id)
        db.session.delete(category)
        db.session.commit()
        flash('Category deleted successfully!')
        return redirect(url_for('categories.show_category'))
    return render_template('delete_category.html', categories=categories)
