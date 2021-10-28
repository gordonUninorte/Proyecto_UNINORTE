import functools
from flask import Flask, render_template, blueprints, request, send_file, redirect, url_for,session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from db import get_db
from markupsafe import escape
from  datetime import datetime
import sqlite3

# from formularios import formularioMensaje

salt = "Equipo8"

main= blueprints.Blueprint('main', __name__)

def login_required(view):
    
    @functools.wraps(view)
    def wraped_view(**kwargs):
        if 'correo' not in session:
            return redirect(url_for('main.login'))
        return view(**kwargs)
        print(session['correo'])
    return wraped_view

@main.route('/home_admin')
@login_required
def home_admin():
    
    return render_template("home_admin.html")

@main.route('/home_estudiante')
@login_required
def home_estudiante():
    
    return render_template("home_estudiantes.html")

@main.route('/actividades_estu')
@login_required
def actividades_estu():
    
    return render_template("actividades_estu.html")


@main.route('/materia', methods=('GET', 'POST'))
@login_required
def materia():
    if request.method == 'POST':
        
        nombre = escape(request.form['username'])
        db = get_db()
        db.execute("insert into Materias (Materias) values(?)",(nombre))
        db.commit()
        db.close()
        
    
    return render_template("ingresar_materia.html")


@main.route('/curso', methods=('GET', 'POST'))
@login_required
def curso():
    if request.method == 'POST':
        
        curso = escape(request.form['username1'])
        db = get_db()
        db.execute("insert into cursos (cursos) values (?)",[curso])
        db.commit()
        db.close()

    return render_template("ingresar_grupo.html")


@main.route('/evaluar_actividades', methods=['GET', 'POST'])
@login_required
def evaluar_actividades():

    if request.method == 'GET':       

        db = get_db()
        db.row_factory = sqlite3.Row
        result2 = db.execute('select * from Materias').fetchall()
        result3 = db.execute('select * from Actividades').fetchall()
        db.commit()
        db.close()

        listado2 = []
        for item in result2:
            listado2.append({j: item[j] for j in item.keys()})
                  
        listado3 = []
        for item in result3:
            listado3.append({k: item[k] for k in item.keys()})
            return render_template("evaluar_actividades.html", lista2 = listado2, lista3 = listado3)
      

    if request.method =='POST':
        identificacion = escape(request.form['id'])        
        db = get_db()
        
        resultado=db.execute('select nombre from usuarios where identificacion = ? ', (identificacion,)).fetchall()
        prueba=resultado[0][0]
        db.row_factory = sqlite3.Row
        result2 = db.execute('select * from Materias').fetchall()
        result3 = db.execute('select * from Actividades').fetchall()
        listado2 = []
        for item in result2:
            listado2.append({j: item[j] for j in item.keys()})
                  
        listado3 = []
        for item in result3:
            listado3.append({k: item[k] for k in item.keys()})
        db.commit()
        db.close()
        return render_template("evaluar_actividades.html", user= prueba, user1= identificacion, lista2 = listado2, lista3 = listado3)
        
        
    # if request.method =='POST':
    #     db = get_db()
        # Materia = escape(request.form['Materias'])
        # Actividad = escape(request.form['Actividades'])
        # nombre = escape(request.form['nombre'])
        # Identificacion = escape(request.form['Identificacion'])
        # Calificacion = escape(request.form['Calificacion'])
        # Comentario = escape(request.form['textarea'])
        
        # db.execute("insert into Evaluar_actividades (id_materias, id_actividades, nombre_estudiante, identificacion_estudiante, calificacion, comentario) values( ?, ?, ?, ?, ?, ?)",(Materia, Actividad, nombre, Identificacion, Calificacion, Comentario))
        # db.commit()
        # db.close() 
        # return render_template("evaluar_actividades.html", user= resultado[0][0], user1= identificacion, lista2 = listado2, lista3 = listado3)
              
    if request.method == "GET":       
        print("Entre al metodo get")
        db = get_db()
        db.row_factory = sqlite3.Row
        result2 = db.execute('select * from Materias').fetchall()
        result3 = db.execute('select * from Actividades').fetchall()
        db.commit()
        db.close()

        listado2 = []
        for item in result2:
            listado2.append({j: item[j] for j in item.keys()})
                  
        listado3 = []
        for item in result3:
            listado3.append({k: item[k] for k in item.keys()})
            return render_template("evaluar_actividades.html", lista2 = listado2, lista3 = listado3)
      

    if request.method == "POST":
        identificacion = escape(request.form['id'])        
        db = get_db()
        resultado=db.execute('select nombre from usuarios where identificacion = ? ', (identificacion,)).fetchall()
        db.row_factory = sqlite3.Row
        result2 = db.execute('select * from Materias').fetchall()
        result3 = db.execute('select * from Actividades').fetchall()
        listado2 = []
        for item in result2:
            listado2.append({j: item[j] for j in item.keys()})
                  
        listado3 = []
        for item in result3:
            listado3.append({k: item[k] for k in item.keys()})

        Materia = escape(request.form['Materias'])
        Actividad = escape(request.form['Actividades'])
        nombre = resultado[0][0] #escape(request.form['nombre'])
        Identificacion = identificacion#escape(request.form['Identificacion'])
        Calificacion = escape(request.form['Calificacion'])
        Comentario = escape(request.form['textarea'])
        
        db.execute("insert into Evaluar_actividades (id_materias, id_actividades, nombre_estudiante, identificacion_estudiante, calificacion, comentarios) values( ?, ?, ?, ?, ?, ?)",(Materia, Actividad, nombre, Identificacion, Calificacion, Comentario))
        db.commit()
        db.close()
        print("Entre al metodo post")
        print(resultado[0][0])
        return render_template("evaluar_actividades.html", user= resultado[0][0], user1= identificacion, lista2 = listado2, lista3 = listado3)        



@main.route('/asignar_docentes', methods=('GET', 'POST'))
def asignar_docentes():
   
    if request.method =='POST':
        identificacion = escape(request.form['id'])        
        db = get_db()
        resultado=db.execute('select nombre from usuarios where identificacion = ? ', (identificacion,)).fetchall()
        db.commit()
        db.close()    
        return render_template("asignar_docentes.html", user= resultado[0][0], user1= identificacion)
   
    return render_template('asignar_docentes.html')

@main.route( '/', methods=['GET', 'POST'] )

def login():
    """Función que maneja la ruta login.Responde a los métodos GET y POST.

        Parameters:
        Ninguno

        Returns:
        login.html si es invocada con el método GET. 
        Redirecciona a  main.ajax si es invocada con POST y la validación es verdadera.

    """
    print("entro a login")
    

    if request.method =='POST':
        
        print("entro a POST")

        correo = escape(request.form['correo'])
        password =  escape(request.form['userPassword'])
        db = get_db()
       
        user = db.execute('select * from usuarios where correo = ? ', (correo,)).fetchone()
        db.commit()
        db.close()


        if user is not None:
            
            print("entro a USER")

            print(user[4])# las columnas de la base de datos se enumeran desde 0, la clave está en la columna4
            #agregamos SALT
            password = password + correo
            
            sw = check_password_hash(user[5], password)

            if(sw):
                session['correo'] = user[4]
                session['nombre'] = user[3]
                session['identificacion'] = user[2]
                session['id_usuario'] = user[0]
                session['id_rol'] = user[1]  
                if(user[1] == 'Administrador'):         
                    return redirect(url_for('main.home_admin'))
                elif(user[1] == 'Docente'):           
                    return redirect(url_for('main.home_docentes'))
                elif(user[1] == 'Estudiante'):           
                    return redirect(url_for('main.home_estudiante'))              
            

        flash('Usuario o clave incorrectos.', 'errodeLogin')
        return render_template('login.html')

    return render_template('login.html')    

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
        foto = request.files['cargar_foto']
        
        now = datetime.now()                        # --> Colocar la fecha como nombre a la foto
        tiempo = now.strftime("%Y%H%M%S")           #
                                                
        if foto.filename!='': 
            nuevoNombreFoto=tiempo+foto.filename  #
            foto.save("static/assets/img/"+ nuevoNombreFoto) 
        rutafoto= "static/assets/img/"+ nuevoNombreFoto
    ############################################## 
    
    
        
        db = get_db()
        #agregar SALT
        password = password + correo
        password = generate_password_hash(password)
        db.execute("insert into usuarios (id_rol, identificacion, nombre, correo, password, foto) values( ?, ?, ?, ?, ?, ?)",(id_rol, identificacion, nombre, correo, password, rutafoto))
        db.commit()
        db.close()       
    
    return render_template("ingresar_admin.html")


@main.route('/home_docentes', methods=['GET', 'POST'])
@login_required
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

@main.route('/Crear_actividades', methods=['GET', 'POST'])
@login_required
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
    
    if request.method == 'POST':
        
        actividad = escape(request.form['id'])
        materia = escape(request.form['Materias'])
        curso = escape(request.form['curso'])
        
        
        
        db = get_db()
        db.execute("insert into Actividades (id_materia, id_curso, nombre_actividad) values( ?, ?, ?)",(materia, curso, actividad))
        db.commit()
        db.close()
        
        
    return render_template("Crear_actividades.html")

@main.route('/logout/')
@login_required
def logout():
   session.clear()

   return redirect(url_for('main.login'))

