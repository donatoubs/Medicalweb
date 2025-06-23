from flask import Blueprint, render_template, request, redirect, url_for, flash
# Asegúrate de importar el nuevo modelo Medico
from app.models import Medico

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Podrías pasar algunos médicos destacados a la página de inicio
    medicos_destacados = Medico.query.limit(4).all()
    return render_template('index.html', medicos=medicos_destacados)

@main_bp.route('/equipo')
def equipo():
    """
    Esta función ahora obtiene todos los médicos de la base de datos
    y los pasa a la plantilla para ser mostrados dinámicamente.
    """
    try:
        # Consulta todos los registros de la tabla 'medicos'
        lista_medicos = Medico.query.all()
        # Pasa la lista de médicos a la plantilla bajo la variable 'medicos'
        return render_template('equipo.html', medicos=lista_medicos)
    except Exception as e:
        flash('Error al cargar la información de los médicos.', 'danger')
        print(f"Error en la ruta /equipo: {e}")
        return render_template('equipo.html', medicos=[])


@main_bp.route('/servicios')
def servicios():
    """Muestra la página de servicios."""
    # Con esta ruta simple, la lógica para mostrar/ocultar servicios
    # debe ser manejada con JavaScript en el frontend.
    return render_template('servicios.html')


@main_bp.route('/contacto')
def contacto():
    """Muestra la página de contacto."""
    return render_template('contacto.html')

@main_bp.route('/terminos')
def terminos():
    """Muestra la página de terminoscontacto."""
    return render_template('terminos.html')
