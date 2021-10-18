function guardarDato(){
    //capturando variables
    const nombre = document.getElementById("nombre").value;
    const email = document.getElementById("email").value;
    const total = document.getElementById("total").value;
    
    const datos = {
        'email': email,
        'total': total,
    };
    //Almacenando los datos
    localStorage.setItem(nombre, JSON.stringify(datos));
    // Borrando los datos
    document.getElementById("nombre").value = "";
    document.getElementById("email").value = "";
    document.getElementById("total").value = "";
    //actualizando lista
    actualizarDatos();
}

function recuperarDato(){
    var nombre = document.getElementById("nombre").value;
    localStorage.getItem(nombre);
    document.getElementById("email").value = JSON.parse(localStorage.getItem(nombre)).email;
    document.getElementById("total").value = JSON.parse(localStorage.getItem(nombre)).total;
}

function actualizarDatos(){
        if ( (localStorage.nombre != undefined) && (localStorage.movil != undefined) ) {
            document.getElementById("datos").innerHTML = "Nombre: " + localStorage.nombre + "<br> Email: " + localStorage.email + "<b> total: " + localStorage.total;
        } else {
            document.getElementById("datos").innerHTML = "No existen datos registrados";
        }
}