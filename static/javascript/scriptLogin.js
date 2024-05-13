const pass = document.getElementById("exampleInputPassword1");
const icon = document.querySelector(".bx");
let failedAttempts = 0;

icon.addEventListener("click", e => {
    if (pass.type == "password") {
        pass.type = "text";
        icon.classList.add('bx-show')
        icon.classList.remove('bx-hide')
    } else {
        pass.type = "password";
        icon.classList.remove('bx-show')
        icon.classList.add('bx-hide')
    }
});

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('exampleInputEmail1').value;
    const password = document.getElementById('exampleInputPassword1').value;

    // Verifica si la contraseña cumple con los requisitos
    if (password.length < 8 || !(/[A-Z]/.test(password))) {
        alert('La contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula.');
        return; // Detiene el proceso si la contraseña no cumple con los requisitos
    }

    // Lógica de autenticación ficticia
    if (username === 'usuario' && password === 'contraseña') {
        alert('Login exitoso');
    } else {
        failedAttempts++;
        alert('Login fallido. Intentos restantes: ' + (3 - failedAttempts));

        // Bloquea el formulario después de 3 intentos fallidos
        if (failedAttempts >= 3) {
            document.getElementById('exampleInputEmail1').disabled = true;
            document.getElementById('exampleInputPassword1').disabled = true;
            document.querySelector('button[type="submit"]').disabled = true;
            alert('Has excedido el número máximo de intentos. Por favor, inténtalo más tarde.');
        }
    }
});
