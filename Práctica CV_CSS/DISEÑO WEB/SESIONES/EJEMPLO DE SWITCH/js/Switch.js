function insertaSwitch() {
    var n, n1, n2;
    document.write(' Resultado: <br>');
    n = prompt('Seleccione una operación matemática:', '');
    n = parseInt(n);
    switch (n) {
        case 1:
            n1 = prompt('Ingrese el primer número:', '');
            n2 = prompt('Ingrese el segundo número:', '');
            Suma(n1, n2);
            break;
        case 2:
            n1 = prompt('Ingrese el primer número:', '');
            n2 = prompt('Ingrese el segundo número:', '');
            Resta(n1, n2);
            break;
        case 3:
            n1 = prompt('Ingrese el primer número:', '');
            n2 = prompt('Ingrese el segundo número:', '');
            Multiplicación(n1, n2);
            break;
        case 4:
            n1 = prompt('Ingrese el primer número:', '');
            n2 = prompt('Ingrese el segundo número:', '');
            División(n1, n2);
            break;
    }
}

function Suma(num1, num2) {
    var suma;
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);
    suma = num1 + num2;
    document.write('La suma es: ', suma);
}
function Resta(num1, num2) {
    var resta;
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);
    resta = num1 - num2;
    document.write('La resta es: ', resta);
}
function Multiplicación(num1, num2) {
    var multiplicación;
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);
    multiplicación = num1 * num2;
    document.write('La multiplicación es: ', multiplicación);
}
function División(num1, num2) {
    var división;
    num1 = parseFloat(num1);
    num2 = parseFloat(num2);
    división = num1 / num2;
    document.write('La división es: ', división);
}
