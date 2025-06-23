# Importa 'db' desde el archivo local db.py
from .db import db

class Especialidad(db.Model):
    __tablename__ = 'especialidades'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)

    # La relación se define en el modelo Cita, aquí no es necesaria.