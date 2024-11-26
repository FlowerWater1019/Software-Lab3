# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .extensions import db
from .models import Category, Task
from sqlalchemy import inspect
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['WTF_CSRF_ENABLED'] = False
    db.init_app(app)
    
    from app.categories import categories_bp
    app.register_blueprint(categories_bp, url_prefix='/')

    from app.tasks import tasks_bp
    app.register_blueprint(tasks_bp, url_prefix='/')
    
    from app.timeline import timeline_bp
    app.register_blueprint(timeline_bp, url_prefix='/')
    
    with app.app_context():
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        if len(tables) == 0:
            db.create_all()
            c1 = Category(name='Work')
            c2 = Category(name='Personal')
            c3 = Category(name='Study')
            db.session.add(c1)
            db.session.add(c2)
            db.session.add(c3)
            db.session.commit()
            
    return app
