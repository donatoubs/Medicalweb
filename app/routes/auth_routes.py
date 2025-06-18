from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.forms.login_form import LoginForm, RegistroForm
from app import db
from flask_login import login_required, login_user, logout_user, current_user

auth_bp = Blueprint('auth', __name__)  # Asegúrate de que esté aquí

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    registro_form = RegistroForm()

    if request.method == 'POST':
        if 'submit_login' in request.form and login_form.validate_on_submit():
            usuario = User.query.filter_by(correo=login_form.correo.data).first()
            if usuario and check_password_hash(usuario.clave, login_form.clave.data):
                login_user(usuario)
                flash('Inicio de sesión exitoso', 'success')
                return redirect(url_for('main.index'))
            else:
                flash('Correo o clave incorrectos', 'danger')

        elif 'submit_register' in request.form and registro_form.validate_on_submit():
            existente = User.query.filter_by(correo=registro_form.correo.data).first()
            if existente:
                flash('Este correo ya está registrado', 'warning')
            else:
                nuevo_usuario = User(
                    nombre=registro_form.nombre.data,  # Nuevo campo
                    correo=registro_form.correo.data,
                    clave=generate_password_hash(registro_form.clave.data),
                    dni=registro_form.dni.data
                )
                db.session.add(nuevo_usuario)
                db.session.commit()
                flash('Usuario registrado exitosamente', 'success')
                return redirect(url_for('auth.login'))

    return render_template('login.html', login_form=login_form, registro_form=registro_form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))