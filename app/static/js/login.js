document.addEventListener('DOMContentLoaded', function() {
    
    // Seleccionamos los elementos del DOM
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const showRegisterLink = document.getElementById('show-register');
    const showLoginLink = document.getElementById('show-login');

    // Nos aseguramos de que los elementos existan antes de añadir los listeners
    if (showRegisterLink) {
        showRegisterLink.addEventListener('click', function(e) {
            e.preventDefault(); // Evita que el enlace '#' recargue la página
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
        });
    }

    if (showLoginLink) {
        showLoginLink.addEventListener('click', function(e) {
            e.preventDefault(); // Evita que el enlace '#' recargue la página
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
        });
    }

    // ¡Hemos eliminado toda la lógica de validación de aquí!
    // Ahora el formulario se enviará directamente al servidor, que es lo que queremos.
});
