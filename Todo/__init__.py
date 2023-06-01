from flask import Flask,render_template


def createApp():

    app = Flask(__name__)

    # CONFIGURACION DEL PROYECTO
    app.config.from_mapping(
        DEBUG=True,
        SECRETE_KEY='dev'
    )

    # REGSITRO DE BLUPRINT
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
