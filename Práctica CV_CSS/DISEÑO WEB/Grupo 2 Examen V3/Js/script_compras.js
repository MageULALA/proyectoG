window.onload = function () {
const baseDeDatos = [{
        id: 1,
        nombre: 'Metro de cable',
        precio: 25,
        imagen:"Img/cable.jpg"
    },
    {
        id: 2,
        nombre: 'Sierra electrica',
        precio: 150,
        imagen:"Img/cierra.jpg"
    },
    {
        id: 3,
        nombre: 'Conjunto de destornilladores',
        precio: 80,
        imagen:"Img/destornilladores.jpg"
    },
    {
        id: 4,
        nombre: 'Gata hidraulica',
        precio: 120,
        imagen:"Img/gata.jpg"

    },
    {
        id: 5,
        nombre: 'Conjunto de herramientas de mano',
        precio: 70,
        imagen:"Img/herramientas-caja.jpg"

    },
    {
        id: 6,
        nombre: 'Taladro de mano',
        precio: 100,
        imagen:"Img/taladro.jpg"

    },
    {
        id: 7,
        nombre: 'Soldadora',
        precio: 300,
        imagen:"Img/soldadora.png"

    },
    {
        id: 8,
        nombre: 'Guantes',
        precio: 10,
        imagen:"Img/guantes.jpg"

    },{
        id: 9,
        nombre: 'Pulidora',
        precio: 200,
        imagen:"Img/pulidora.jpg"

    }


];

let carrito = [];
let total = 0;
const cont_items = document.querySelector('#items');
const cont_carrito = document.querySelector('#compras');
const cont_total = document.querySelector('#total');
const cont_botonVaciar = document.querySelector('#boton-vaciar');
const cont_botonEnviarCompra = document.querySelector('#enviar_compra');
const miLocalStorage = window.localStorage;


function renderizarProductos() {
    baseDeDatos.forEach((info) => {
        // Estructura
        const miNodo = document.createElement('div');
        miNodo.classList.add('card', 'col-sm-4');
        miNodo.style.border="solid black 2px";
        // Body
        const miNodoCardBody = document.createElement('div');
        miNodoCardBody.classList.add('card-body');
        // Titulo
        const miNodoTitle = document.createElement('h5');
        miNodoTitle.classList.add('card-title');
        miNodoTitle.textContent = info.nombre;
        // Imagen
        const miNodoImagen = document.createElement('img');
        miNodoImagen.classList.add('img-fluid');
        miNodoImagen.setAttribute('src', info.imagen);
        // Precio
        const miNodoPrecio = document.createElement('p');
        miNodoPrecio.classList.add('card-text');
        miNodoPrecio.textContent = 'S/ ' + info.precio;
        // Boton 
        const miNodoBoton = document.createElement('button');
        miNodoBoton.classList.add('btn', 'btn-primary');
        miNodoBoton.textContent = '+';
        miNodoBoton.setAttribute('marcador', info.id);
        miNodoBoton.addEventListener('click', agregar_carrito);
        // Insertamos
        miNodoCardBody.appendChild(miNodoImagen);
        miNodoCardBody.appendChild(miNodoTitle);
        miNodoCardBody.appendChild(miNodoPrecio);
        miNodoCardBody.appendChild(miNodoBoton);
        miNodo.appendChild(miNodoCardBody);
        cont_items.appendChild(miNodo);
    });
}

/**
* Evento para añadir un producto al carrito de la compra
*/
function agregar_carrito(evento) {
    // Anyadimos el Nodo a nuestro carrito
    carrito.push(evento.target.getAttribute('marcador'))
    // Calculo el total
    calcularTotal();
    // Actualizamos el carrito 
    renderizarCarrito();
    // Actualizamos el LocalStorage
    guardarCarritoEnLocalStorage();
}

/**
* Dibuja todos los productos guardados en el carrito
*/
function renderizarCarrito() {
    // Vaciamos todo el html
    cont_carrito.textContent = '';
    // Quitamos los duplicados
    const carritoSinDuplicados = [...new Set(carrito)];
    // Generamos los Nodos a partir de carrito
    carritoSinDuplicados.forEach((item) => {
        // Obtenemos el item que necesitamos de la variable base de datos
        const miItem = baseDeDatos.filter((itemBaseDatos) => {
            // ¿Coincide las id? Solo puede existir un caso
            return itemBaseDatos.id === parseInt(item);
        });
        // Cuenta el número de veces que se repite el producto
        const numeroUnidadesItem = carrito.reduce((total, itemId) => {
            // ¿Coincide las id? Incremento el contador, en caso contrario no mantengo
            return itemId === item ? total += 1 : total;
        }, 0);
        // Creamos el nodo del item del carrito
        const miNodo = document.createElement('li');
        miNodo.classList.add('list-group-item', 'text-right', 'mx-2');
        miNodo.textContent = `${numeroUnidadesItem} x ${miItem[0].nombre} - S/. ${miItem[0].precio}`;
        // Boton de borrar
        const miBoton = document.createElement('button');
        miBoton.classList.add('btn', 'btn-dark', 'mx-3');
        miBoton.textContent = 'x';

        miBoton.dataset.item = item;
        miBoton.addEventListener('click', borrarItemCarrito);
        // Mezclamos nodos
        miNodo.appendChild(miBoton);
        cont_carrito.appendChild(miNodo);
    });
}

/**
* Evento para borrar un elemento del carrito
*/
function borrarItemCarrito(evento) {
    // Obtenemos el producto ID que hay en el boton pulsado
    const id = evento.target.dataset.item;
    // Borramos todos los productos
    carrito = carrito.filter((carritoId) => {
        return carritoId !== id;
    });
    // volvemos a renderizar
    renderizarCarrito();
    // Calculamos de nuevo el precio
    calcularTotal();
    // Actualizamos el LocalStorage
    guardarCarritoEnLocalStorage();

}

/**
* Calcula el precio total teniendo en cuenta los productos repetidos
*/
function calcularTotal() {
    // Limpiamos precio anterior
    total = 0;
    // Recorremos el array del carrito
    carrito.forEach((item) => {
        // De cada elemento obtenemos su precio
        const miItem = baseDeDatos.filter((itemBaseDatos) => {
            return itemBaseDatos.id === parseInt(item);
        });
        total = total + miItem[0].precio;
    });
    // Renderizamos el precio en el HTML
    cont_total.textContent = total.toFixed(2);
}

/**
* Varia el carrito y vuelve a dibujarlo
*/
function vaciarCarrito() {
    // Limpiamos los productos guardados
    carrito = [];
    // Renderizamos los cambios
    renderizarCarrito();
    calcularTotal();
    // Borra LocalStorage
    localStorage.clear();

}

function guardarCarritoEnLocalStorage () {
    miLocalStorage.setItem('carrito', JSON.stringify(carrito));
}

function cargarCarritoDeLocalStorage () {
    // ¿Existe un carrito previo guardado en LocalStorage?
    if (miLocalStorage.getItem('carrito') !== null) {
        // Carga la información
        carrito = JSON.parse(miLocalStorage.getItem('carrito'));
    }
}

function escribir_info() {
    if (document.getElementById("nombre").value== 0) {
        document.getElementById("info_nombre").innerHTML="______________________________";
    } else{
        document.getElementById("info_nombre").innerHTML=document.getElementById("nombre").value;
    }

    if (document.getElementById("email").value== 0) {
        document.getElementById("info_email").innerHTML="______________________________";
    } else{
        document.getElementById("info_email").innerHTML=document.getElementById("email").value;
    }

    document.getElementById("info_total").innerHTML="Total: S/ "+total.toFixed(2);
}

// Eventos
cont_botonVaciar.addEventListener('click', vaciarCarrito);
cont_botonEnviarCompra.addEventListener('click', escribir_info);

// Inicio
cargarCarritoDeLocalStorage();
renderizarProductos();
calcularTotal();
renderizarCarrito();
}


