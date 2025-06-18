document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('citaForm');
    const select = document.getElementById('especialidad');

    // Cargar especialidades dinámicamente desde el backend
    fetch('/especialidades')
        .then(res => res.json())
        .then(data => {
            if (data.length === 0) {
                select.disabled = true;
                return;
            }

            data.forEach(esp => {
                const option = document.createElement('option');
                option.value = esp.id;
                option.textContent = esp.nombre;
                select.appendChild(option);
            });

            select.disabled = false;
        })
        .catch(() => {
            select.disabled = true;
        });

    // Validación de campos antes de enviar el formulario
    form.addEventListener('submit', e => {
        const nombre = document.getElementById('nombre').value.trim();
        const email = document.getElementById('email').value.trim();
        const telefono = document.getElementById('telefono').value.trim();
        const especialidad = select.value;
        const fecha = document.getElementById('fecha').value;

        if (!nombre || !email || !telefono || !especialidad || !fecha) {
            e.preventDefault();
            alert('Por favor, completa todos los campos antes de enviar la cita.');
        }
    });
});
