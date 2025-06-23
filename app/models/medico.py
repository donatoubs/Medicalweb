from .db import db

class Medico(db.Model):
    __tablename__ = 'medicos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    foto_url = db.Column(db.String(255), default='imagenes/default-avatar.png')
    biografia = db.Column(db.Text)
    horarios = db.Column(db.String(255))
    
    # Clave foránea que conecta con la tabla 'especialidades'
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)
    
    # Relación que nos permite acceder fácilmente a la información de la especialidad
    # Por ejemplo: mi_medico.especialidad.nombre
    especialidad = db.relationship('Especialidad')

    def __repr__(self):
        return f'<Medico {self.nombre} {self.apellido}>'
