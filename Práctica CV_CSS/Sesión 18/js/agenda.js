function guardardatos{
    localStorage.nombre = document.getElementById("nombre").value;
    localStorage.movil = document.getElementById("movil").value;

}


function recuperardatos{
    if ((localStorage.nombre != undefined) && (localStorage.movil != undefined)) {
        document.getElementById("datos").innerHTML = "Nombre: " + localStorage.nombre + " Numero celular: " + localStorage.movil;
    } else {
        document.getElementById("datos").innerHTML = "No has ingresado tu nombre ni numero celular"
    }
}


