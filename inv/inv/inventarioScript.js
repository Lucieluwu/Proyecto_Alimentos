let mostrador = document.getElementById("mostrador");
let seleccion = document.getElementById("seleccion");
let contenedorOpciones = document.getElementById("contenedorOpciones");
let imgSeleccionada = document.getElementById("img");
let modeloSeleccionado = document.getElementById("modelo");
let descripSeleccionada = document.getElementById("descripcion");
let cantidadSeleccionado = document.getElementById("cantidad");

function cargar(item){
    quitarBordes();
    mostrador.style.width = "72%";
    seleccion.style.marginTop = "14%";
    seleccion.style.width = "30%";
    seleccion.style.opacity = "1";
    item.style.border = "2px solid green";

    imgSeleccionada.src = item.getElementsByTagName("img")[0].src;
    modeloSeleccionado.innerHTML = item.getElementsByTagName("p")[0].innerHTML;
    descripSeleccionada.innerHTML = "Descripción del modelo ";
    cantidadSeleccionado.innerHTML = item.getElementsByTagName("span")[0].innerHTML;
}

function cerrar(){
    mostrador.style.width = "100%";
    seleccion.style.width = "0%";
    seleccion.style.opacity = "0";
    quitarBordes();
}

function quitarBordes(){
    var items = document.getElementsByClassName("item");
    for(i=0;i <items.length; i++){
        items[i].style.border = "none";
    }
}

// Escuchar el evento scroll para actualizar la posición de la selección y del contenedor de opciones
window.addEventListener('scroll', function() {
    actualizarPosicion();
});

// Función para actualizar la posición de la selección y del contenedor de opciones
function actualizarPosicion() {
    // Obtener la posición vertical actual del viewport
    const scrollOffset = window.pageYOffset;

    // Aplicar el desplazamiento al contenedor de opciones
    contenedorOpciones.style.top = scrollOffset + 'px';

    // Solo aplicar el desplazamiento al contenedor de selección si está abierto
    if (seleccion.style.width !== "0%") {
        seleccion.style.top = scrollOffset + 'px';
    }
}

