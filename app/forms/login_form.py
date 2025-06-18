from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    clave = PasswordField('Clave', validators=[DataRequired(), Length(min=6)])
    submit_login = SubmitField('Iniciar Sesión')

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(min=2, max=100)])  # Nuevo campo
    correo = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    clave = PasswordField('Clave', validators=[DataRequired(), Length(min=6)])
    confirmar_clave = PasswordField('Confirmar Clave', validators=[
        DataRequired(), EqualTo('clave', message='Las claves deben coincidir')
    ])
    dni = StringField('Número de DNI', validators=[DataRequired(), Length(min=8, max=20)])
    submit_register = SubmitField('Registrarse')