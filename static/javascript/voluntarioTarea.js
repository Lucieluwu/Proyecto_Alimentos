
    document.getElementById("btnAsignar").addEventListener("click", function() {
        var idact = this.getAttribute("data-idact"); // Obtener el valor del atributo data-idact
        window.location.href = "/vol_dashboard/" + idact; // Redireccionar a la ruta en Flask con el valor de idact
        alert("Exito al marcar la tarea como hecha")
    });