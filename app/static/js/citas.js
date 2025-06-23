document.addEventListener('DOMContentLoaded', function() {
    
    // --- LÓGICA DE VALIDACIÓN DEL FORMULARIO ---
    const citaForm = document.getElementById('citaForm');
    const errorContainer = document.getElementById('form-errors');

    if (citaForm) {
        citaForm.addEventListener('submit', function(event) {
            // Prevenimos el envío automático del formulario para validarlo primero
            event.preventDefault();

            // Limpiamos errores anteriores
            errorContainer.innerHTML = '';
            let errors = [];

            // Campos requeridos
            const nombrePaciente = document.getElementById('nombre_paciente').value.trim();
            const apellidoPaciente = document.getElementById('apellido_paciente').value.trim();
            const emailPaciente = document.getElementById('email_paciente').value.trim();
            const especialidad = document.getElementById('especialidad').value;
            const medico = document.getElementById('medico').value;
            const fecha = document.getElementById('fecha').value;
            const telefono = document.getElementById('telefono_paciente').value;

            // Verificación general de campos obligatorios
            if (!nombrePaciente || !apellidoPaciente || ! emailPaciente || ! especialidad || !medico || !fecha || ! telefono) {
                errors.push('Todos los campos son obligatorios!');
            }

            // Decisión final: enviar o mostrar errores
            if (errors.length > 0) {
                // Si hay errores, los mostramos
                const errorList = errors.map(error => `<li>${error}</li>`).join('');
                errorContainer.innerHTML = `<ul>${errorList}</ul>`;
                errorContainer.style.display = 'block';
            } else {
                // Si no hay errores, enviamos el formulario
                errorContainer.style.display = 'none';
                citaForm.submit();
            }
        });
    }

    // --- LÓGICA PARA CONFIGURAR EL CAMPO DE FECHA Y HORA ---
    const fechaInput = document.getElementById('fecha');
    if (fechaInput) {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        const minDateTime = now.toISOString().slice(0, 16);
        fechaInput.min = minDateTime;
        fechaInput.step = 1800; // 30 minutos

        fechaInput.addEventListener('input', function(e) {
            const selectedDate = new Date(e.target.value);
            const minutes = selectedDate.getMinutes();
            if (minutes !== 0 && minutes !== 30) {
                const roundedMinutes = Math.round(minutes / 30) * 30;
                if (roundedMinutes === 60) {
                    selectedDate.setHours(selectedDate.getHours() + 1);
                    selectedDate.setMinutes(0);
                } else {
                    selectedDate.setMinutes(roundedMinutes);
                }
                const correctedDate = new Date(selectedDate.getTime() - (selectedDate.getTimezoneOffset() * 60000));
                e.target.value = correctedDate.toISOString().slice(0, 16);
            }
        });
    }

    // --- LÓGICA PARA CARGAR MÉDICOS DINÁMICAMENTE ---
    const especialidadSelect = document.getElementById('especialidad');
    const medicoSelect = document.getElementById('medico');
    if (especialidadSelect && medicoSelect) {
        especialidadSelect.addEventListener('change', function() {
            // (La lógica para cargar médicos se mantiene igual)
            const especialidadId = this.value;
            medicoSelect.innerHTML = '<option value="">Cargando...</option>';
            medicoSelect.disabled = true;
            if (especialidadId) {
                fetch(`/api/medicos_por_especialidad/${especialidadId}`)
                    .then(response => response.json())
                    .then(data => {
                        medicoSelect.disabled = false;
                        medicoSelect.innerHTML = '<option value="" disabled selected>-- Seleccione un médico --</option>';
                        if (data.length > 0) {
                            data.forEach(medico => {
                                const option = document.createElement('option');
                                option.value = medico.id;
                                option.textContent = medico.nombre;
                                medicoSelect.appendChild(option);
                            });
                        } else {
                            medicoSelect.innerHTML = '<option value="">No hay médicos</option>';
                            medicoSelect.disabled = true;
                        }
                    });
            } else {
                medicoSelect.innerHTML = '<option value="">-- Elija especialidad --</option>';
                medicoSelect.disabled = true;
            }
        });
    }
});
