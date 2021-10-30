
//var userNameInput = document.formularioRegistro.username;
//window.status="Hola mundo";
function validar()
{
    var userIDInput = document.formularioRegistro.id;
    var userNameInput = document.formularioRegistro.username;
    var correoInput = document.formularioRegistro.correo;
    var userRolInput = document.formularioRegistro.rol;
    var passWordInput = document.formularioRegistro.userPassword;
   

    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

    var swErrores=false;

    console.log(userNameInput.value + "-"+passWordInput.value+"-"+correoInput.value);



    if(userNameInput.value.length == 0 || userNameInput.value.length < 8)
    {
        //alert("El nombre de usuario debe tener mínimo 8 caracteres.");
        document.getElementById("errorUsername").innerHTML="El nombre de usuario debe tener mínimo 8 caracteres.";
        userNameInput.focus();
        //document.getElementById("botonEnviar").disabled=true;
        swErrores=true;
    }

    if(passWordInput.value.length == 0 || passWordInput.value.length < 8)
    {
        //alert("La clave debe tener mínimo 8 caracteres.");
        document.getElementById("errorPassword").innerHTML="La clave debe tener mínimo 8 caracteres.";
        passWordInput.focus();
        swErrores=true;
    }

    if(!correoInput.value.match(formato_email))
    {
        //alert("Por favor escriba un correo válido.");
        document.getElementById("errorMail").innerHTML=" correo no válido.";
        correoInput.focus();
        swErrores=true;
    }

    if( swErrores==true)
    {
        return false;
    }
    else{
        return true;
    }
}

// validacion de no dejar campos vacios en el login

function validarLogin()                                 
{ 
             var userName = document.formularioLogin.correo;
			 var userPassword = document.formularioLogin.userPassword;	
             		 
			 var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;

             var swError=false;
			 
        
             if (!userName.value.match(formato_email)) {
                 document.getElementById('errorUsername').innerHTML="formato no valido Email.";  
                 userName.focus();
                 swError=true;
             } else {
                document.getElementById('errorUsername').innerHTML="";
             }
                   
             /*if (userPassword.value == ""){ 
                 document.getElementById('errorPassword').innerHTML="Por favor escriba una clave.";  
                 userPassword.focus();
                 swError=true; 
                 //return false; 
             }else{
                 document.getElementById('errorPassword').innerHTML="";  
             }*/
			
			if (swError==true) {
                
                return false;
             }
             else{

                return true;
             }
			 
			 
}

function mostrar(){
    document.getElementById("userPassword").type="text";
}

function ocultar (){
    document.getElementById("userPassword").type="password";
}

/*function verClave()
{
    console.log('Mostrar clave');

    var passWordInput = document.getElementById('userPassword');
    passWordInput.type="text";
}

function ocultarClave()
{
    console.log('Ocultar clave');
    var passWordInput = document.getElementById('userPassword');
    passWordInput.type="password";

    
}

function ocultarVerClave()
{
    var passWordInput = document.getElementById('userPassword');
    var tipo = passWordInput.type;

    console.log(tipo);

    if(tipo=="text")
    {
        passWordInput.type="password";
    }

    if(tipo == "password")
    {
        passWordInput.type="text";
    }
}*/
 