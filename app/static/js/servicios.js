// Función para mostrar solo el servicio seleccionado
function mostrarServicio(servicio) {
  // Ocultamos todos los servicios
  const servicios = document.querySelectorAll('.service-item');
  servicios.forEach(function(item) {
    item.style.display = 'none';
  });

  // Mostramos la sección correspondiente
  document.getElementById(servicio).style.display = 'block';
}
