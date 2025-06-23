from .db import db

class Cita(db.Model):
    """
    Modelo para la tabla 'citas'. Cada instancia representa una cita agendada,
    vinculando un paciente, un médico y el usuario que realizó la reserva.
    """
    __tablename__ = 'citas'
    
    id = db.Column(db.Integer, primary_key=True)
    
    # Datos del paciente para quien es la cita
    nombre_paciente = db.Column(db.String(100), nullable=False)
    apellido_paciente = db.Column(db.String(100), nullable=False)
    email_paciente = db.Column(db.String(120))
    telefono_paciente = db.Column(db.String(10))
    
    # Detalles de la cita
    fecha = db.Column(db.DateTime, nullable=False)
    motivo = db.Column(db.Text)
    estado = db.Column(db.String(50), default='Confirmada')
    
    # Claves Foráneas
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    agendado_por_usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    # Relaciones para acceder a los objetos completos
    # Permite hacer: mi_cita.medico.nombre
    medico = db.relationship('Medico')
    # Permite hacer: mi_cita.agendado_por.nombre
    agendado_por = db.relationship('User')

    def __repr__(self):
        return f'<Cita para {self.nombre_paciente} con Dr. {self.medico.apellido}>'
