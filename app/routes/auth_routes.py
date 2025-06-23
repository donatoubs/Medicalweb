from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
# Asegúrate de importar todos los modelos y formularios necesarios
from app.models import db, User
from app.forms.login_form import LoginForm, RegistroForm

auth_bp = Blueprint('auth', __name__)

# --- RUTA DE LOGIN ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    registro_form = RegistroForm() # Se pasa para que el template lo tenga disponible

    # Lógica para procesar el envío del formulario de login
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user and check_password_hash(user.clave, login_form.clave.data):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')
            
    # Si es una petición GET o el login falla, se muestra la página
    return render_template('login.html', login_form=login_form, registro_form=registro_form)

# --- RUTA DE REGISTRO (LA QUE FALTABA) ---
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Creamos instancias de ambos formularios por si la validación falla
    login_form = LoginForm()
    registro_form = RegistroForm()

    # Se procesa solo si el formulario de registro es enviado y válido
    if registro_form.validate_on_submit():
        # Recolectamos los datos del formulario de registro
        nombre = registro_form.nombre.data
        apellido = registro_form.apellido.data
        dni = registro_form.dni.data
        email = registro_form.email.data
        clave = registro_form.clave.data
        
        # Verificamos que el email y el DNI no estén ya en uso
        if User.query.filter_by(email=email).first():
            flash('El correo electrónico ya está registrado.', 'danger')
        elif User.query.filter_by(dni=dni).first():
            flash('El DNI ya está registrado.', 'danger')
        else:
            # Creamos el nuevo usuario
            hashed_password = generate_password_hash(clave, method='pbkdf2:sha256')
            nuevo_usuario = User(
                nombre=nombre,
                apellido=apellido,
                dni=dni,
                email=email,
                clave=hashed_password
            )
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('¡Cuenta creada exitosamente! Ahora puedes iniciar sesión.', 'success')
            return redirect(url_for('auth.login'))

    # Si la validación falla, se renderiza de nuevo la página de login
    # Los errores del formulario se mostrarán automáticamente en la plantilla.
    return render_template('login.html', login_form=login_form, registro_form=registro_form)

# --- RUTA DE LOGOUT ---
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('auth.login'))
