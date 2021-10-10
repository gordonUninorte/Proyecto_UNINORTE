 function validaarFormulario()                                 
 {   
     var userId = document.formularioRegistro.id;
     var userName = document.formularioRegistro.username;
     var userRol = document.formularioRegistro.rol;
     var userCurso = document.formularioRegistro.curso;
     var userPassword = document.formularioRegistro.password;	
     var correo = document.formularioRegistro.correo;	
     var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;	
     
     var swError= false;
     
     
     if (userId.value == "" || userId.value.length <7){ 
         document.getElementById('errorId').innerHTML="Por favor escriba Solo números.";  
         userId.focus(); 
         userId.style.left = "20px";
         swError = true;
         return false; 
     }else{
         document.getElementById('errorId').innerHTML="";  
     }
     

     /////////////////////////////////
     if (userName.value == "" || userName.value.length <8){ 
        document.getElementById('errorName').innerHTML="Por favor escriba un nombre con mínimo 8 caracteres.";  
        userName.focus(); 
        userName.style.left = "20px";
        swError = true;
        return false; 
    }else{
        document.getElementById('errorName').innerHTML="";  
    }

    ////////////////////////////////////
    ///////////////////////////////////////
    if (userRol.value == "" || userRol.value.length ==""){ 
        document.getElementById('errorRol').innerHTML="Por favor Seleccione un privilegio para el Usuario.";  
        userRol.focus(); 
        userRol.style.left = "20px";
        swError = true;
        return false; 
    }else{
        document.getElementById('errorRol').innerHTML="";  
    }

    ///////////////////////////////////////


    ////////////////////////////////////////

    if (userCurso.value == "" || userCurso.value.length <7){ 
        document.getElementById('errorCurso').innerHTML="Por favor Seleccione un curso para el Usuario.";  
        userCurso.focus(); 
        userCurso.style.left = "20px";
        swError = true;
        return false; 
    }else{
        document.getElementById('errorCurso').innerHTML="";  
    }

    //////////////////////////////////////////     
     
     if (!correo.value.match(formato_email)) {
         document.getElementById('errorEmail').innerHTML="Por favor escriba un correo válido.";  
         correo.focus(); 
         swError = true;
         return false; 
     }
     else
     {
        document.getElementById('errorEmail').innerHTML="";  
     }
     
     
     if(swError == true)
     {
        return false; 
     }

     if (userPassword.value == "" || userPassword.value.length <8){ 
        document.getElementById('errorPassword').innerHTML="Por favor escriba una clave con mínimo 8 caracteres.";  
        userPassword.focus(); 
        swError = true;
        return false; 
        
    }else{
        document.getElementById('errorPassword').innerHTML="";  
    }
     
     
 }

function mostrar()
{
document.getElementById("userPassword").type="text";
}

function ocultar()
{
document.getElementById("userPassword").type="password";
}
