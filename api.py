from flask import jsonify, blueprints
from flask.globals import request

from db import get_db



api = blueprints.Blueprint('api',__name__)


@api.route('/mensaje/')
def mensaje():
    """Función que maneja la ruta de mensaje.

        Parameters:
        Ninguno

        Returns:
        Json con el contenido de la lista mensajes.

    """
    from mensaje import getMensajes
    return jsonify(getMensajes())

@api.route('/agregarMensaje/', methods=['POST'])
def menagregarMensajesaje():
    
    if request.method=='POST':

        print(request.json)
        inf = request.json
        usuario = inf['usuario']
        asunto = inf['asunto']
        mensaje = inf['mensaje']

        db = get_db()
        db.execute("insert into mensajesV1 ( usuario, asunto, mensaje) values( ?, ?, ?)",(usuario, asunto, mensaje))
        db.commit()
        db.close()

    
    return jsonify({'mensaje':'ok'})