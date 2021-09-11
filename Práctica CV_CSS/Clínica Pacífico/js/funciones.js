function guardarDato(){
    //capturando variables
    const nombre = document.getElementById("nombre").value;
    const movil = document.getElementById("dCita").value;
    const email = document.getElementById("turno").value;
    
    const datos = {
        'dCita': movil,
        'turno': email,
    };
    //Almacenando los datos
    localStorage.setItem(nombre, JSON.stringify(datos));
    // Borrando los datos
    document.getElementById("DNI").value = "";
    document.getElementById("nombre").value = "";
    document.getElementById("apellidos").value = "";
    document.getElementById("fechaNa").value = "";
    document.getElementById("lugarNa").value = "";
    document.getElementById("dir").value = "";
    document.getElementById("distr").value = "";
    document.getElementById("prov").value = "";
    document.getElementById("dept").value = "";
    document.getElementById("espcMe").value = "";
    document.getElementById("dCita").value = "";
    document.getElementById("turno").value = "";
    
    
    //actualizando lista
    actualizarDatos();
}

function recuperarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.getItem(nombre);
    document.getElementById("dCita").value = JSON.parse(localStorage.getItem(nombre)).dCita;
    document.getElementById("turno").value = JSON.parse(localStorage.getItem(nombre)).turno;
}

function eliminarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.removeItem(nombre);
    actualizarDatos();
}

function eliminarTodo(){
    localStorage.clear();
    actualizarDatos();
}

function actualizarDatos(){
    var registro = "";
    if (localStorage.length === 0){
        registro += '<li>Vacío</li>';
    } else{
        for (var i = 0; i<=localStorage.length-1; i++ ){
            var key = localStorage.key(i);
            registro += '<li>' + '<span class="nom">' + key + '</span>'
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).dCita + '</span>' 
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).turno + '</span>' + '</li><br>';
        }
    }
    document.getElementById('contactos').innerHTML=registro;
}