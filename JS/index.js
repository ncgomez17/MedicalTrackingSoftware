let map;

function initMap() {
  maps = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 8,
  });
}
window.onload = function() {
    //funciones a ejecutar
    const boton = document.querySelector('#boton');
    const menu = document.querySelector('#menu');

    boton.addEventListener('click', () => {
        console.log("Me diste click");
        menu.classList.toggle('hidden');
    });
};