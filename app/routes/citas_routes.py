from flask import Blueprint, jsonify, request, redirect, url_for, flash, render_template
from app.models.especialidad import Especialidad
from app.models.cita import Cita
from app.models.db import db
import datetime

citas_bp = Blueprint('citas_bp', __name__)

@citas_bp.route('/especialidades')
def obtener_especialidades():
    especialidades = Especialidad.query.all()
    return jsonify([{'id': e.id, 'nombre': e.nombre} for e in especialidades])

@citas_bp.route('/citas')
def mostrar_formulario_cita():
    # Renderiza la plantilla del formulario de citas
    return render_template('citas.html')

@citas_bp.route('/submit_cita', methods=['POST'])
def submit_cita():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    telefono = request.form.get('telefono')
    especialidad_id = request.form.get('especialidad')
    fecha_str = request.form.get('fecha')

    print(f"Received data: {nombre}, {email}, {telefono}, {especialidad_id}, {fecha_str}")

    if not (nombre and email and telefono and especialidad_id and fecha_str):
        flash("Todos los campos son obligatorios", "danger")
        print("Error: campos obligatorios faltantes")
        return redirect(url_for('citas_bp.mostrar_formulario_cita'))

    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        flash("Fecha inválida", "danger")
        print("Error: fecha inválida")
        return redirect(url_for('citas_bp.mostrar_formulario_cita'))

    especialidad = Especialidad.query.get(especialidad_id)
    if not especialidad:
        flash("Especialidad seleccionada no existe", "danger")
        print("Error: especialidad no existe")
        return redirect(url_for('citas_bp.mostrar_formulario_cita'))

    nueva_cita = Cita(
        nombre=nombre,
        email=email,
        telefono=telefono,
        especialidad_id=especialidad.id,
        fecha=fecha
    )

    try:
        db.session.add(nueva_cita)
        db.session.commit()
        flash("Cita agendada exitosamente", "success")
        print(f"Cita guardada con id: {nueva_cita.id}")
        return redirect(url_for('main.index'))
    except Exception as e:
        db.session.rollback()
        flash("Error al guardar la cita", "danger")
        print(f"Error al guardar cita: {e}")
        return redirect(url_for('citas_bp.mostrar_formulario_cita'))
