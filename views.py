from flask import blueprints, render_template,request

main=blueprints.Blueprint('main',__name__)

@main.route('/', methods=('GET', 'POST') )
def index():
    if(request.method=='POST'):
        cad=""
           
        cad= request.form['username']        
        
        cad= cad + "-" +request.form['password']
        if((request.form['username'] == 'jesus@equipo8.edu.co') & (request.form['password']=='Prueba123')): 
            return render_template('home_admin.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Lila@equipo8.edu.co') & (request.form['password']=='Prueba123')): 
            return render_template('home_docentes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Marvin@equipo8.edu.co') & (request.form['password']=='Prueba123')): 
            return render_template('home_estudiantes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Germania@equipo8.edu.co') & (request.form['password']=='Prueba123')): 
            return render_template('home_docentes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Giam@equipo8.edu.co') & (request.form['password']=='Prueba123')): 
            return render_template('home_estudiantes.html')#'Hola, Mundo!'
        else:
            return render_template('login.html')

    return render_template('login.html')

###############################   ADMIN  ###############################      
@main.route('/home_admin', methods=('GET', 'POST'))
def home_admin():
    
    return render_template("home_admin.html")

##############################  GESTIONAR PERÍODO  ################################
@main.route('/periodo', methods=('GET', 'POST'))
def periodo():
    
    return render_template("ingresar_periodo.html")

##############################  GESTIONAR MATERIA  ################################
@main.route('/materia', methods=('GET', 'POST'))
def materia():
    
    return render_template("ingresar_materia.html")

##############################  GESTIONAR FACULTAD  ################################
@main.route('/asignar_docentes', methods=('GET', 'POST'))
def asignar_docentes():
    
    return render_template("asignar_docentes.html")

##############################  GESTIONAR FACULTAD  ################################
@main.route('/curso', methods=('GET', 'POST'))
def grupo():
    
    return render_template("ingresar_grupo.html")

###############################  GESTIONAR ADMIN  ###############################    
@main.route('/admin', methods=('GET', 'POST'))
def admin():
    
    return render_template("ingresar_admin.html")

@main.route('/edit_admin', methods=('GET', 'POST'))
def edit_admin():
    
    return render_template("edit_admin.html")

  ###############################  DOCENTES  #############################      
@main.route('/home_docentes', methods=('GET', 'POST'))
def home_docentes():
    
    return render_template("home_docentes.html")

  ############################### INGRESAR DOCENTES  #############################      
@main.route('/ingresar_docentes', methods=('GET', 'POST'))
def ingresar_docentes():
    
    return render_template("ingresar_docentes.html")

  ############################### EDIT DOCENTES  #############################      
@main.route('/edit_docentes', methods=('GET', 'POST'))
def edit_docentes():
    
    return render_template("edit_docentes.html")

 ############################### ASIGNAR ESTUDIANTE  #############################      
@main.route('/ingresar_estudiante', methods=('GET', 'POST'))
def ingresar_estudiante():
    
    return render_template("ingresar_estudiante.html")

############################### EDIT ESTUDIANTE  #############################      
@main.route('/edit_estudiante', methods=('GET', 'POST'))
def edit_estudiante():
    
    return render_template("edit_estudiante.html")

############################### CREAR ACTIVIDADES  #############################      
@main.route('/Crear_actividades', methods=('GET', 'POST'))
def Crear_actividades():
    
    return render_template("Crear_actividades.html")

############################### EVALUAR ACTIVADES  #############################      
@main.route('/evaluar_actividades', methods=('GET', 'POST'))
def evaluar_actividades():
    
    return render_template("evaluar_actividades.html")
############################### HOME ESTUDIANTE  #############################      
@main.route('/home_estudiantes', methods=('GET', 'POST'))
def home_estudiantes():
    
    return render_template("home_estudiantes.html")

############################### VER CALIFICACIÓN  #############################      
@main.route('/actividades_estu', methods=('GET', 'POST'))
def actividades_estu():
    
    return render_template("actividades_estu.html")