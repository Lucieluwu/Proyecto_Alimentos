let mostrador = document.getElementById("mostrador");
let seleccion = document.getElementById("seleccion");
let contenedorOpciones = document.getElementById("contenedorOpciones");
let imgSeleccionada = document.getElementById("img");
let modeloSeleccionado = document.getElementById("modelo");
let descripSeleccionada = document.getElementById("descripcion");
let cantidadSeleccionado = document.getElementById("cantidad");

let ids = [];
let max = 0;

function almacenarDatos() {
    let sw = validarNumero();
    // Capturar los valores del formulario
    if (sw) {
        var idalim = document.getElementById('idalim').value;
        var cantidad = document.getElementById('cantidad-input').value;

        // Crear un objeto con los datos capturados y agregarlo a la lista
        var datosFormulario = {
            idalim: idalim,
            cantidad: cantidad
        };
        ids.push(datosFormulario);

        document.getElementById('cantidad-input').value = 1;
        console.log(ids)
        cerrar();
    }
    else{
        cerrar();
    }
}

function enviarDatos() {
    // Convertir la lista de datos a JSON
    var datosJSON = JSON.stringify(ids);

    // Enviar los datos JSON al servidor
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/recibe_sol', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Manejar la respuesta del servidor si es necesario
            console.log('Datos enviados correctamente');
        }
    };
    xhr.send(datosJSON);
}
function validarNumero() {
    var inputNumero = parseInt(document.getElementById('cantidad-input').value);
    var maximoPermitido = parseInt(max); // Cambia 100 por el número máximo permitido (X)

    if (inputNumero > maximoPermitido) {
      alert("El número ingresado supera el máximo permitido de " + maximoPermitido);
      document.getElementById('cantidad-input').value = 1;
      return false;
    }
    return true;
  }

function cargar(item){
    quitarBordes();
    mostrador.style.width = "72%";
    seleccion.style.marginTop = "14%";
    seleccion.style.width = "30%";
    seleccion.style.opacity = "1";
    item.style.border = "2px solid green";

    var stock = item.getAttribute('data-stock');
    var idalim = item.getAttribute('data-id');

    max = stock;

    document.getElementById('cantidad-input').setAttribute('max', stock);
    document.getElementById('idalim').setAttribute('value', idalim);

    imgSeleccionada.src = item.getElementsByTagName("img")[0].src;
    modeloSeleccionado.innerHTML = item.getElementsByTagName("p")[0].innerHTML;
    //descripSeleccionada.innerHTML = "Descripción del modelo ";
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

