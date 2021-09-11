window.onload = function () {

    const bd = [{
            id: 1,
            nombre: 'Borderlands New Mad Loot Box',
            precio: 80,
            imagen:"Img/cable.jpg"
        },{
            id: 2,
            nombre: 'Sierra electrica',
            precio: 178,
            imagen:"Img/cierra.jpg"
        },{
            id: 3,
            nombre: 'Conjunto de destornilladores',
            precio: 20,
            imagen:"Img/destornilladores.jpg"
        },{
            id: 4,
            nombre: 'Gata hidraulica',
            precio: 230,
            imagen:"Img/gata.jpg"
        },{
            id: 5,
            nombre: 'Conjunto de herramientas de mano',
            precio: 10,
            imagen:"Img/herramientas-caja.jpg"
        },{
            id: 6,
            nombre: 'Taladro de mano',
            precio: 200,
            imagen:"Img/taladro.jpg"
        }
    ];
    
    var carrito=[];
    var total= 0;
    var nuevo_total=0;
    var descuento=0;

    // Cajas////

    const cont_botonCanjear=document.querySelector('#canjear');
    const cont_carrito = document.querySelector('#compras');
    const cont_total = document.querySelector('#sub_total');
    const cont_nuevo_total = document.querySelector('#nuevo_total');
    const cont_botonVaciar = document.querySelector('#vaciar_compras');
    const almacenLocal = localStorage;
    const boton_compras = document.querySelector('#boton_compras');

    
    function mostrarProductos() {

        bd.forEach((info) => {

            if (info.id==1) {
                const cursorBoton = document.createElement('button');
                cursorBoton.classList.add('col-6','btn','btn-dark','boton_usuario','mx-auto','d-flex','justify-content-center','mb-0' );
                cursorBoton.textContent = 'Agregar al Carrito';
                cursorBoton.setAttribute('clave_primaria', info.id);
                cursorBoton.addEventListener('click', agregar_carrito);
                document.querySelector('#caja').appendChild(cursorBoton);
            }else{
                
                const cursorBoton2 = document.createElement('button');
                cursorBoton2.classList.add('col-6','btn','btn-dark','boton_usuario','mx-auto','d-flex','justify-content-center','mb-0' );
                cursorBoton2.textContent = 'Agregar al Carrito';
                cursorBoton2.setAttribute('clave_primaria', info.id);
                cursorBoton2.addEventListener('click', agregar_carrito);
                document.querySelector('#caja_cod').appendChild(cursorBoton2);

            }

        });
    

    }
    
    function calcularTotal() {
        total = 0;
        carrito.forEach((item) => {
            const articulo = bd.filter((itemBaseDatos) => {
                return itemBaseDatos.id === parseInt(item);
            });
            total = total + articulo[0].precio;
        });
        cont_total.textContent = total.toFixed(2);
    }

///////////////////
    cont_botonCanjear.addEventListener('click', canjearCodigo);

    function canjearCodigo() {

        descuento=0;
        var codigo= document.getElementById('text_codigo').value;

        if (codigo=="Orange") {
            
            descuento=total-(total/2);

            document.getElementById('promocion').innerHTML = descuento.toFixed(2);

            calcularNuevoTotal()
            document.getElementById('text_codigo').value="";
        }
    }


    function calcularNuevoTotal() {
        nuevo_total = 0;
        carrito.forEach((item) => {
            const articulo = bd.filter((itemBaseDatos) => {
                return itemBaseDatos.id === parseInt(item);
            });
            nuevo_total = nuevo_total + articulo[0].precio;
        });

        
        nuevo_total=nuevo_total-descuento;
        cont_nuevo_total.textContent = nuevo_total.toFixed(2);
    }


    
    function agregar_carrito(evento) {
        carrito.push(evento.target.getAttribute('clave_primaria'))
        calcularTotal();
        calcularNuevoTotal()
        mostrarCarrito();
        almacenLocal.setItem('carrito', JSON.stringify(carrito));
    }
    
    
    function mostrarCarrito() {
        cont_carrito.textContent = '';
        const carritoSinDuplicados = [...new Set(carrito)];
        carritoSinDuplicados.forEach((item) => {
            const articulo = bd.filter((itemBaseDatos) => {
                return itemBaseDatos.id === parseInt(item);
            });
            const contadorUnidades = carrito.reduce((total, itemId) => {
                return itemId === item ? total += 1 : total;
            }, 0);
    
            const nodo = document.createElement('li');
            nodo.classList.add('text-right', 'mx-2','list-group-item');
            nodo.textContent = contadorUnidades + ' ---> ' + articulo[0].nombre + '- S/. ' + articulo[0].precio;
    
            const bton = document.createElement('button');
            bton.classList.add('btn', 'btn-dark', 'mx-3');
            bton.textContent = 'x';
            bton.style.float='right'
            bton.dataset.item = item;
            bton.addEventListener('click', borrarItemCarrito);
            nodo.appendChild(bton);
            cont_carrito.appendChild(nodo);
        });
    }
    
    
    function borrarItemCarrito(evento) {
        const id = evento.target.dataset.item;
        carrito = carrito.filter((carritoId) => {
            return carritoId !== id;
        });
        mostrarCarrito();
        calcularTotal();
        calcularNuevoTotal()
        almacenLocal.setItem('carrito', JSON.stringify(carrito));
    }
    
    
    cont_botonVaciar.addEventListener('click', vaciarCarrito);
    function vaciarCarrito() {
        carrito = [];
        mostrarCarrito();
        calcularTotal();
        descuento=0;
        calcularNuevoTotal()
        nuevo_total=0;
        document.getElementById('promocion').innerHTML =nuevo_total.toFixed(2);
        localStorage.clear();
    }
    
    
    function revisarBaseDatos() {
        if (almacenLocal.getItem('carrito') !== null) {
            carrito = JSON.parse(almacenLocal.getItem('carrito'));
        }
    }
    
    document.getElementById('permitir').addEventListener('click', function(e) {

        cont_botonVaciar.disabled=false;
       
      });


    boton_compras.addEventListener('click', mostrarCarrito);
    boton_compras.addEventListener('click', calcularTotal);
    boton_compras.addEventListener('click', calcularNuevoTotal);
    boton_compras.addEventListener('click',  revisarBaseDatos);

    revisarBaseDatos();
    mostrarProductos();
    calcularTotal();
    mostrarCarrito();
    calcularNuevoTotal()
    }
    
    
    