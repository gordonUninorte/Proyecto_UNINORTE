from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))          	
def hola_mundo():   

    if(request.method=='POST'):
        cad=""
    
        
        cad= request.form['username']        
        cad= cad + "-" +request.form['password']
        if((request.form['username'] == 'jesus@equipo8.edu.co') & (request.form['password']=='prueba1')): 
            return render_template('home_admin.html')#'Administrador!'
        elif((request.form['username'] == 'Lila@equipo8.edu.co') & (request.form['password']=='prueba1')): 
            return render_template('Docentes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Marvin@equipo8.edu.co') & (request.form['password']=='prueba1')): 
            return render_template('Estudiantes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Germania@equipo8.edu.co') & (request.form['password']=='prueba1')): 
            return render_template('Docentes.html')#'Hola, Mundo!'
        elif((request.form['username'] == 'Giam@equipo8.edu.co') & (request.form['password']=='prueba1')): 
            return render_template('home_docentes.html')#'Hola, Mundo!'
        else:
            return render_template('index.html')
        
    return render_template('index.html')#'Hola, Mundo!'	
        
@app.route('/home_admin', methods=('GET', 'POST'))
def home_admin():
    
    return render_template("home_admin.html")


@app.route('/admin', methods=('GET', 'POST'))
def admin():
    
    return render_template("admin.html")


@app.route('/home_docentes', methods=('GET', 'POST'))
def home_docentes():
    
    return render_template("home_docentes.html")

@app.route('/admin_docentes', methods=('GET', 'POST'))
def admin_docentes():
    
    return render_template("admin_docentes.html")


if __name__== "__main__":
    app.run(debug=True);
