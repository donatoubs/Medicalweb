from flask import Flask
from flask_login import LoginManager
from config import Config
# Importa la instancia db desde su ubicación correcta
from .models.db import db

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializa db con la app
    db.init_app(app)
    login_manager.init_app(app)

    # Importar modelos ANTES de registrar las rutas que los usan
    from .models.user import User
    from .models.cita import Cita
    from .models.especialidad import Especialidad

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Importar y registrar blueprints
    from .routes.main_routes import main_bp
    from .routes.auth_routes import auth_bp
    from .routes.citas_routes import citas_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(citas_bp) # Agregamos un prefijo por claridad

    return app