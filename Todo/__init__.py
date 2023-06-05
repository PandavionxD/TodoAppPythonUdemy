from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def createApp():

    app = Flask(__name__)

    # CONFIGURACION DEL PROYECTO
    app.config.from_mapping(
        DEBUG=True,
        SECRETE_KEY='dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todoApp.db"
    )

    # INICIALIZAR CONEXION A BASE DE DATOS
    db.init_app(app)

    # REGSITRO DE BLUPRINT
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    # MIGRAR MODELOS A LA BASE DE DATOS 
    with app.app_context():
        db.create_all()

    return app
