const pass = document.getElementById("password");
const icon = document.getElementById("icon"); // Se cambió la selección del icono

icon.addEventListener("click", e => {
    if (pass.type == "password") {
        pass.type = "text";
        icon.classList.add('bx-show');
        icon.classList.remove('bx-hide');
    } else {
        pass.type = "password";
        icon.classList.remove('bx-show');
        icon.classList.add('bx-hide');
    }
});

const pass1 = document.getElementById("r_password");
const icon1 = document.getElementById("icon1"); // Se cambió la selección del icono

icon1.addEventListener("click", e => { // Cambió el nombre del listener a icon1
    if (pass1.type == "password") {
        pass1.type = "text";
        icon1.classList.add('bx-show');
        icon1.classList.remove('bx-hide');
    } else {
        pass1.type = "password";
        icon1.classList.remove('bx-show');
        icon1.classList.add('bx-hide');
    }
});
