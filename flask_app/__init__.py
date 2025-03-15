from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    from .models import Person # Przed db.create_all() nalezy zaimportowac klase modelowa

    with app.app_context():
        db.create_all()  # Tworzy tabele automatycznie

    from .routes import main  # Importowanie tras
    app.register_blueprint(main)  # Rejestracja tras

    return app