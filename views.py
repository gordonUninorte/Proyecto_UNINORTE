import functools
from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
from markupsafe import escape
import sqlite3

from formularios import formularioMensaje

salt = "Equipo8"

main= blueprints.Blueprint('main', __name__)

# @main.route('/', methods=('GET', 'POST'))          	
# def hola_mundo():   

#     if(request.method=='POST'):
#         cad=""
    
        
#         cad= request.form['correo']        
#         cad= cad + "-" +request.form['userPassword']
#         if((request.form['correo'] == 'jesus@equipo8.edu.co') & (request.form['userPassword']=='Prueba123')): 
#             return render_template('home_admin.html')#'Hola, Mundo!'
#         elif((request.form['correo'] == 'lila@equipo8.edu.co') & (request.form['userPassword']=='Prueba123')): 
#             return render_template('home_docentes.html')#'Hola, Mundo!'

#         else:
#             return render_template('login.html')
        
#     return render_template('login.html')#'Hola, Mundo!'

@main.route( '/' )
def hello_world():
    """Función que maneja la raiz del sitio web.

        Parameters:
        Ninguno

        Returns:
        Plantilla index.html

    """

    return render_template('login.html')


def login_required(view):

    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'correo' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)
    
    return wraped_view

@main.route('/home_admin', methods=('GET', 'POST'))
def home_admin():
    
    return render_template("home_admin.html")


@main.route('/login/', methods=['GET', 'POST'])
def login():
    """Función que maneja la ruta login.Responde a los métodos GET y POST.

        Parameters:
        Ninguno

        Returns:
        login.html si es invocada con el método GET. 
        Redirecciona a  main.ajax si es invocada con POST y la validación es verdadera.

    """

    if request.method =='POST':

        correo = escape(request.form['correo'])
        password =  escape(request.form['userPassword'])
        db = get_db()
       
        user = db.execute('select * from usuarios where correo = ? ', (correo,)).fetchone()
        db.commit()
        db.close()


        if user is not None:

            print(user[4])# las columnas de la base de datos se enumeran desde 0, la clave está en la columna4
            #agregamos SALT
            password = password + correo
            
            sw = check_password_hash(user[5], password)

            if(sw):
                session['correo'] = user[4]
                session['nombre'] = user[3]
                session['identificacion'] = user[2]
                session['id_rol'] = 'Administrador'
                session['id_usuario'] = user[0]
                
                print(session['nombre'])
                           
                
                # return redirect(url_for('main.ajax'))
                return redirect(url_for('home_admin.html'))
            # return render_template('home_admin.html')

        flash('Usuario o clave incorrectos.', 'errodeLogin')
        return render_template('login.html')

    return render_template('login.html')





#   ###############################   INGRESAR USUARIOS  ###############################      
# @main.route('/home_admin', methods=('GET', 'POST'))
# def home_admin():
    
#     return render_template("home_admin.html")

@main.route('/admin', methods=('GET', 'POST'))
def admin():
    if request.method == 'GET':
    
    
        db = get_db()
        db.row_factory = sqlite3.Row
        result = db.execute('select * from rol').fetchall()
        db.commit()
        db.close()

        listado = []
        for item in result:
            listado.append({k: item[k] for k in item.keys()})
        return render_template("ingresar_admin.html", lista=listado)
        
    if request.method == 'POST':
    
        id_rol = escape(request.form['rol'])
        identificacion = escape(request.form['id'])
        nombre = escape(request.form['username'])
        correo = escape(request.form['correo'])
        password = escape(request.form['userPassword'])
        # foto = escape(request.form['foto'])
        
        db = get_db()
        #agregar SALT
        password = password + correo
        password = generate_password_hash(password)
        db.execute("insert into usuarios (id_rol, identificacion, nombre, correo, password) values( ?, ?, ?, ?, ?)",(id_rol, identificacion, nombre, correo, password))
        db.commit()
        db.close()
    
    return render_template("ingresar_admin.html")

#################################################### MOSTRAR DOCENTES  ####################

@main.route('/home_docentes', methods=('GET', 'POST'))
def home_docentes():

    
    if request.method == 'GET':  
        
        db = get_db()
        db.row_factory = sqlite3.Row
        result = db.execute('select * from usuarios').fetchall()
        db.commit()
        db.close()

        listado = []
        for item in result:
            listado.append({k: item[k] for k in item.keys()})
        return render_template("home_docentes.html", lista=listado)     

    #     db = get_db() 
    #     cursor = db.cursor()
    #     cursor.execute('SELECT * FROM usuarios')
    #     data = cursor.fetchall()
    #     db.commit()    
    
    # return render_template("home_docentes.html", usuarios=data)



# @main.route( '/' )
# def hello_world():
#     """Función que maneja la raiz del sitio web.

#         Parameters:
#         Ninguno

#         Returns:
#         Plantilla index.html

#     """

#     return render_template('login.html')


# def login_required(view):

#     @functools.wraps(view)
#     def wraped_view(**kwargs):
#         if 'correo' not in session:
#             return redirect(url_for('main.login'))
#         return view(**kwargs)
    
#     return wraped_view



# @main.route('/login/', methods=['GET', 'POST'])
# def login():
#     """Función que maneja la ruta login.Responde a los métodos GET y POST.

#         Parameters:
#         Ninguno

#         Returns:
#         login.html si es invocada con el método GET. 
#         Redirecciona a  main.ajax si es invocada con POST y la validación es verdadera.

#     """

#     if request.method =='POST':
        

#         correo = escape(request.form['correo'])
#         clave =  escape(request.form['userPassword'])
#         db = get_db()
       
#         user = db.execute('select * from usuarios where correo = ? ', (correo,)).fetchone()
#         db.commit()
#         db.close()


#         if user is not None:

#             print(user[4])# las columnas de la base de datos se enumeran desde 0, la clave está en la columna4
#             #agregamos SALT
#             clave = clave + correo
            
#             sw = check_password_hash(user[4], clave)

#             if(sw):
#                 session['usuario'] = user[2]
#                 session['nombre'] = user[1]
#                 session['id'] = user[0]
#                 session['role'] = 'admin'
           
                
#                 return redirect(url_for('main.ajax'))

#         flash('Usuario o clave incorrectos.', 'errodeLogin')
#         return render_template('login.html')

#     return render_template('login.html')



# @main.route('/ajax/')
# @login_required
# def ajax():
#     """Función que maneja la ruta ajax.

#         Parameters:
#         Ninguno

#         Returns:
#         ajax.html 

#     """
#     return render_template('ajax.html')

# @main.route('/otra/')
# def otra():
#     return 'otra pagina'

@main.route('/evaluar_actividades')
def evaluar_actividades():
    
    if request.method == 'GET':       

        db = get_db()
        db.row_factory = sqlite3.Row
        result = db.execute('select * from Actividades').fetchall()
        db.commit()
        db.close()

        listado = []
        for item in result:
            listado.append({k: item[k] for k in item.keys()})
    return render_template("evaluar_actividades.html", lista=listado)


@main.route('/Crear_actividades')
def Crear_actividades():
    
    if request.method == 'GET':       

        db = get_db()
        db.row_factory = sqlite3.Row
        result = db.execute('select * from Materias').fetchall()
        result1 = db.execute('select * from cursos').fetchall()
        db.commit()
        db.close()

        listado = []
        for item in result:
            listado.append({j: item[j] for j in item.keys()})
                  
        listado1 = []
        for item in result1:
            listado1.append({k: item[k] for k in item.keys()})
            
        return render_template("Crear_actividades.html", lista = listado, lista1 = listado1)
   
    
@main.route('logout')
def logout():
   session.clear()

   return redirect(url_for('main.login'))

# @main.route('/mensaje/')
# def mensaje():
#     obj = formularioMensaje()
    
#     return render_template('mensaje.html', miformulario= obj )


# @main.route('/usuarios/')
# @login_required
# def usuarios():
   
#      db = get_db()
#      db.row_factory = sqlite3.Row
#      result = db.execute('select * from usuario').fetchall()
#      db.commit()
#      db.close()

#      listado = []
#      for item in result:
#          listado.append({k: item[k] for k in item.keys()})


#      return render_template('listado.html', lista = listado )