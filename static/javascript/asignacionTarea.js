


var datos = [];


function enviarDatos() {
    // Convertir la lista de datos a JSON
    var datosJSON = JSON.stringify(datos);

    // Enviar los datos JSON al servidor
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/asigna_tareas', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Manejar la respuesta del servidor si es necesario
            alert('Asignacion con exito');
        }
    };
    xhr.send(datosJSON);
}
    // Esperar a que el documento esté listo
    $(document).ready(function(){
        // Manejar el clic en el botón "ASIGNAR"
        $('.btnAsignar').click(function(){
            // Mostrar el modal
            $('#modalTabla').modal('show');
        });

        // Manejar el clic en el botón "Cerrar" dentro del modal
        $('#btnCerrar').click(function(){
            // Cerrar el modal
            $('#modalTabla').modal('hide');
        });
    });

    $(document).ready(function(){
        // Manejar el clic en el botón "ASIGNAR" del primer elemento
        $('.envAct').click(function(){
            // Obtener el valor del parámetro del atributo de datos
            var parametro = $(this).data('idact');
            
            // Establecer el valor del parámetro al segundo botón
            $('.asignaVol').data('act', parametro);
            
            // Aquí puedes realizar otras acciones si es necesario
            
            // Por ejemplo, mostrar el valor del parámetro en la consola
            console.log("El valor del parámetro es: " + parametro);
        });
    
        // Otro código JavaScript...
    });

    $(document).ready(function(){
         // Arreglo para almacenar los valores de los voluntarios seleccionados
    
        // Manejar el clic en el botón "ASIGNAR" de los voluntarios
        $('.asignaVol').click(function(){
            var voluntario = $(this).data('vol'); // Obtener el valor del voluntario seleccionado
            var actividad = $(this).data('act'); // Obtener el valor del voluntario seleccionado
            
            info = {voluntario : voluntario, actividad : actividad}

            datos.push(info);
        
            enviarDatos();

            window.location.href = "/dashboard";
        });
    
        // Otra lógica de tu aplicación...
    });