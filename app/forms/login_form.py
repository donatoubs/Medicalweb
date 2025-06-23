from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class RegistroForm(FlaskForm):
    """Formulario para el registro de nuevos usuarios con mensajes de error claros."""
    nombre = StringField('Nombres', 
                         validators=[DataRequired(message="El nombre es obligatorio."), 
                                     Length(min=3, max=100)])
    
    apellido = StringField('Apellidos', 
                           validators=[DataRequired(message="El apellido es obligatorio."), 
                                       Length(min=3, max=100)])
    
    dni = StringField('DNI / Cédula', 
                      validators=[DataRequired(message="El DNI es obligatorio."), 
                                  Regexp('^[0-9]*$', message='El DNI solo debe contener números.'),
                                  Length(min=10, max=10, message="El DNI debe tener 10 dígitos.")])
    
    email = StringField('Correo Electrónico', 
                        validators=[DataRequired(message="El email es obligatorio."), 
                                    Email(message="Por favor, ingrese un email válido.")])
    
    clave = PasswordField('Contraseña', 
                          validators=[DataRequired(message="La contraseña es obligatoria."), 
                                      Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")])
    
    confirmar_clave = PasswordField('Confirmar Contraseña', 
                                    validators=[DataRequired(message="Por favor, confirme la contraseña."), 
                                                EqualTo('clave', message='Las contraseñas no coinciden.')])
    
    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    """Formulario para el inicio de sesión."""
    email = StringField('Correo Electrónico', 
                        validators=[DataRequired(), Email()])
    
    clave = PasswordField('Contraseña', 
                          validators=[DataRequired()])
    
    submit = SubmitField('Iniciar Sesión')
