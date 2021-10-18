function guardarDato(){
    //capturando variables
    const nombre = document.getElementById("nombre").value;
    const movil = document.getElementById("movil").value;
    const email = document.getElementById("email").value;
    
    const datos = {
        'movil': movil,
        'email': email,
    };
    //Almacenando los datos
    localStorage.setItem(nombre, JSON.stringify(datos));
    // Borrando los datos
    document.getElementById("nombre").value = "";
    document.getElementById("movil").value = "";
    document.getElementById("email").value = "";
    //actualizando lista
    actualizarDatos();
}

function recuperarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.getItem(nombre);
    document.getElementById("movil").value = JSON.parse(localStorage.getItem(nombre)).movil;
    document.getElementById("email").value = JSON.parse(localStorage.getItem(nombre)).email;
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
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).movil + '</span>' 
            + '<span class="nom">' + JSON.parse(localStorage.getItem(key)).email + '</span>' + '</li><br>';
        }
    }
    document.getElementById('contactos').innerHTML=registro;
}