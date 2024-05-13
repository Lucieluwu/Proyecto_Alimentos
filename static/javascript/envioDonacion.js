document.addEventListener("DOMContentLoaded", function() {
    const foodData = []; // Almacena temporalmente los datos de los alimentos

    const foodForm = document.getElementById("foodForm");
    const tempDataList = document.getElementById("tempDataList");
    const finishButton = document.getElementById("finishButton");

    foodForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que el formulario se envíe normalmente

        // Captura los datos del formulario y los agrega al array de datos de alimentos
        const formData = new FormData(foodForm);
        const foodItem = {};
        formData.forEach(function(value, key) {
            foodItem[key] = value;
        });

        delete foodItem['tipo'];

        // Obtener el nombre del archivo de imagen
        const imagenInput = document.getElementById('tipo');
        foodItem['imagen'] = imagenInput.files[0].name;

        foodData.push(foodItem);

        // Muestra los datos temporales en la tabla
        renderTempData();

        // Limpia el formulario después de enviar los datos temporalmente
        foodForm.reset();
    });

    finishButton.addEventListener("click", function() {
        // Convertir la lista foodData a formato JSON
        const jsonData = JSON.stringify(foodData);

        // Ejemplo de cómo enviar los datos utilizando fetch
        fetch('/recibe_donacion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: jsonData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al enviar los datos');
            }
            return response.json();
        })
        .then(data => {
            // Después de guardar en la base de datos, puedes limpiar la matriz foodData
            foodData.length = 0;

            // Limpiar la tabla de datos temporales
            tempDataList.querySelector("tbody").innerHTML = "";
            alert("Su donacion se a registrado correctamente");

            window.location.href = "/donador_dashboard";
        })
        .catch(error => {
            console.error('Error:', error);
            alert("Ha ocurrido un error al guardar los datos en la base de datos");
        });
    });


    function renderTempData() {
        // Limpiar la tabla antes de volver a renderizar
        tempDataList.querySelector("tbody").innerHTML = "";

        // Renderizar los datos temporales en la tabla
        foodData.forEach(function(item, index) {
            const row = document.createElement("tr");
            row.classList.add("table-light"); // Añade el estilo de fila alternativo de Bootstrap
            row.innerHTML = `
                <td class="text-center">${item.nombre}</td>
                <td class="text-center">${item.desc}</td>
                <td class="text-center">${item.cat}</td>
                <td class="text-center">
                    <button class="btn btn-danger btn-sm delete-button">Eliminar</button>
                </td>
            `;
            tempDataList.querySelector("tbody").appendChild(row);
        });

        // Asignar el evento onclick de forma dinámica
        assignDeleteEventListeners();
    }

    function deleteTempData(index) {
        // Elimina el elemento correspondiente del array de datos temporales
        foodData.splice(index, 1);

        // Vuelve a renderizar la tabla para reflejar los cambios
        renderTempData();
    }

    // Asignar el evento onclick de forma dinámica
    function assignDeleteEventListeners() {
        const deleteButtons = document.querySelectorAll(".delete-button");
        deleteButtons.forEach((button, index) => {
            button.addEventListener("click", () => {
                deleteTempData(index);
            });
        });
    }
});