from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from app.models import db, Cita, Especialidad, Medico
from datetime import datetime
import traceback

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/citas')
@login_required # Proteger esta ruta, solo usuarios logueados pueden ver el formulario
def pagina_citas():
    """
    Muestra la página del formulario de citas y le pasa la lista
    de todas las especialidades para llenar el primer menú desplegable.
    """
    try:
        especialidades = Especialidad.query.all()
        return render_template('citas.html', especialidades=especialidades)
    except Exception as e:
        flash('Error al cargar la página de citas.', 'danger')
        print(f"Error en pagina_citas: {e}")
        return render_template('citas.html', especialidades=[])

@citas_bp.route('/api/medicos_por_especialidad/<int:especialidad_id>')
@login_required
def get_medicos_por_especialidad(especialidad_id):
    """
    API para que el JavaScript obtenga los médicos de una especialidad específica.
    Devuelve los datos en formato JSON.
    """
    try:
        medicos = Medico.query.filter_by(especialidad_id=especialidad_id).all()
        lista_medicos = [
            {"id": medico.id, "nombre": f"{medico.nombre} {medico.apellido}"}
            for medico in medicos
        ]
        return jsonify(lista_medicos)
    except Exception as e:
        print(f"Error en get_medicos_por_especialidad: {e}")
        return jsonify({"error": "No se pudieron cargar los médicos"}), 500

@citas_bp.route('/citas/submit', methods=['POST'])
@login_required
def submit_cita():
    """Procesa el envío del formulario de citas con la nueva estructura."""
    try:
        # 1. Recolectar datos del paciente desde el formulario
        nombre_paciente = request.form.get('nombre_paciente')
        apellido_paciente = request.form.get('apellido_paciente')
        email_paciente = request.form.get('email_paciente')
        telefono_paciente = request.form.get('telefono_paciente')

        # 2. Recolectar detalles de la cita
        medico_id = request.form.get('medico')
        fecha_str = request.form.get('fecha')
        motivo = request.form.get('motivo')

        # 3. Validación de campos
        if not all([nombre_paciente, apellido_paciente, medico_id, fecha_str]):
            flash('Error: Nombre del paciente, apellido, médico y fecha son obligatorios.', 'danger')
            return redirect(url_for('citas.pagina_citas'))

        # 4. Crear el objeto Cita con la nueva estructura
        fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')

        nueva_cita = Cita(
            nombre_paciente=nombre_paciente,
            apellido_paciente=apellido_paciente,
            email_paciente=email_paciente,
            telefono_paciente=telefono_paciente,
            fecha=fecha_obj,
            motivo=motivo,
            medico_id=int(medico_id),
            # CRUCIAL: Vinculamos la cita al usuario que ha iniciado sesión
            agendado_por_usuario_id=current_user.id
        )

        db.session.add(nueva_cita)
        db.session.commit()
        flash('¡Cita agendada exitosamente para el paciente!', 'success')

    except ValueError:
        db.session.rollback()
        flash('Error: El formato de la fecha es incorrecto.', 'danger')
    except Exception as e:
        db.session.rollback()
        print(f"--- ERROR INESPERADO EN submit_cita ---\n{traceback.format_exc()}")
        flash('Ocurrió un error grave al procesar la cita.', 'danger')

    return redirect(url_for('citas.pagina_citas'))
