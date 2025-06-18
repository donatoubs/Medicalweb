from flask import Blueprint, render_template
from flask_login import current_user
from flask import render_template, Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/equipo')
def equipo():
    return render_template('equipo.html')

@main_bp.route('/servicios')
def servicios():
    return render_template('servicios.html')

@main_bp.route('/citas')
def citas():
    return render_template('citas.html')

@main_bp.route('/contacto')
def contacto():
    return render_template('contacto.html')
