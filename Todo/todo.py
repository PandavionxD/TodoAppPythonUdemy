from flask import Blueprint


# url_prefix = url inicial donde inicia rutas de vistas 
bp = Blueprint('todo',__name__,url_prefix='/todo')


@bp.route('/list')
def index():
    return 'Lista de tareas'


@bp.route('/create')
def create():
    return 'Crear una tarea'


