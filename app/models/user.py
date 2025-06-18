from flask_login import UserMixin
from app import db

class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Nuevo campo
    correo = db.Column(db.String(150), unique=True, nullable=False)
    clave = db.Column(db.String(256), nullable=False)
    dni = db.Column(db.String(10), nullable=False)