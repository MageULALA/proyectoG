function alerta(){
    window.alert("Probando Javascript")
}

function saludar(){
    var nombre= document.getElementById("txt1").value;
    alert("Buenos días" + nombre);
}

function saludo(){
    var nombre= document.getElementById("txt1").value;
    var saludo= "Buenos días " + nombre;
    var contenedor=document.getElementById("divsaludo");
    contenedor.innerHTML= saludo;
}