##########################  APP CON VIEWS  ############

import os
from flask import Flask  

def create_app():
    """Función que crea la aplicación principal. 
       Registra las plantillas de api y views(main) con sus respectivas url.
       Registra un secrete Key con un texto fijo.
       
        Parameters:
        Ninguno

        Returns:
        app de Flask

    """
    app = Flask(__name__)

    app.secret_key = 'Equipo8'#os.urandom( 24 )

    from views import main


    app.register_blueprint(main, url_prefix='/')  
    
    return app 

