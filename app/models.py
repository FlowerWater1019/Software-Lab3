# app/models.py
from .extensions import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tasks = db.relationship('Task', backref='category', lazy=True, cascade='all, delete-orphan')
    
    @property
    def task_count(self):
        return len(self.tasks)
    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)
    details = db.Column(db.Text, nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    need_reminder = db.Column(db.Boolean, default=True)
    ddl_delta = db.Column(db.Integer, default=30)
    
    @property
    def category_name(self):
        return self.category.name if self.category else None
    