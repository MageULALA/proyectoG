//Mostrar una ventana emergente
$(document).ready(function () {

    $("a").click(function (evento) {
        alert("Has pulsado en el enlace.Ahora saldrás de la página de la Usat")
    });
});

//ocultar o mostrar una caja
$("#c1b").click(function () {
        $("#cont1").toggle(1500);
    }, function () {
        $("#cont1").toggle(1500);
    }
);
