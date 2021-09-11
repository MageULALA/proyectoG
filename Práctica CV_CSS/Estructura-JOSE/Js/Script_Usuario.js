var boton_g = document.getElementById('boton_guardar');
var boton_e = document.getElementById('boton_editar');

var t1= document.getElementById('nombres');
var t2= document.getElementById('usuario');
var t3= document.getElementById('fecha');
var t4= document.getElementById('correo');
var t5= document.getElementById('correoAlt');
var t6= document.getElementById('contra');
var t7= document.getElementById('telefono');
var t8= document.getElementById('direccion');





document.getElementById('boton_editar').addEventListener('click', function(e) {

    boton_g.disabled = false;
    t1.disabled = false;
    t2.disabled = false;
    t3.disabled = false;
    t4.disabled = false;
    t5.disabled = false;
    t6.disabled = false;
    t7.disabled = false;
    t8.disabled = false;
    t6.type="text";
  });


  document.getElementById('boton_guardar').addEventListener('click', function(e) {
   
    
    var a = document.getElementById('usuario').value;
    boton_g.disabled = true;
    document.getElementById('nombre_usuario').innerHTML=a;
    t1.disabled = true;
    t2.disabled = true;
    t3.disabled = true;
    t4.disabled = true;
    t5.disabled = true;
    t6.disabled = true;
    t7.disabled = true;
    t8.disabled = true;
    t6.type="password";
    
    
   
    
  });