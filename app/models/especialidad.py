from app import db

class Especialidad(db.Model):
    __tablename__ = 'especialidades'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Especialidad {self.nombre}>'
