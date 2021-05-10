        function onDeviceReady() {
            navigator.geolocation.getCurrentPosition(onSuccess, onError);
        }

        // onSuccess Geolocation
        //
        function onSuccess(position) {
            require([
                "esri/config",
                "esri/Map",
                "esri/views/MapView",
                "esri/tasks/Locator",
                "esri/Graphic"
            ], function (esriConfig, Map, MapView, Locator, Graphic) {


                esriConfig.apiKey = "AAPKb6fd7e4ad313411e8b4c768fec1f9abcDIb5yh0ZJbE-yasP94PBPJUnzDxbrtPq0zvi6ELAG2FWOXiJresduGeuaLKTegRq";

                const map = new Map({
                    basemap: "arcgis-navigation"
                });

                const view = new MapView({
                    container: "viewDiv",
                    map: map,
                    center: [position.coords.longitude, position.coords.latitude], //Longitude, latitude
                    zoom: 13
                });

                const places = ["Elige búsqueda",
                "Hospital", "Medical Clinic", "Doctor"];
                const diccionario = new Map();
                // asignando valores
                diccionario.set("Elige búsqueda", "Elige búsqueda ...");
                diccionario.set("Hospital", "Hospital");
                diccionario.set("Hospital", "Hospital");
                diccionario.set("Medical Clinic", "Clinica");
                diccionario.set("Doctor", "Doctor");

                const select = document.createElement("select", "");
                select.setAttribute("class", "esri-widget esri-select");
                select.setAttribute("style", "width: 175px; font-family: 'Avenir Next W00'; font-size: 1em");

                places.forEach(function (p) {
                    const option = document.createElement("option");
                    option.value = diccionario.get(p);
                    option.innerHTML = diccionario.get(p);
                    select.appendChild(option);
                });

                view.ui.add(select, "top-right");

                const locator = new Locator({
                    url: "http://geocode-api.arcgis.com/arcgis/rest/services/World/GeocodeServer"
                });

                // Find places and add them to the map
                function findPlaces(category, pt) {
                    locator.addressToLocations({
                        location: pt,
                        categories: [category],
                        maxLocations: 25,
                        outFields: ["Place_addr", "PlaceName"]
                    })

                        .then(function (results) {
                            view.popup.close();
                            view.graphics.removeAll();

                            results.forEach(function (result) {
                                view.graphics.add(
                                    new Graphic({
                                        attributes: result.attributes,  // Data attributes returned
                                        geometry: result.location, // Point returned
                                        symbol: {
                                            type: "simple-marker",
                                            color: "#000000",
                                            size: "12px",
                                            outline: {
                                                color: "#ffffff",
                                                width: "2px"
                                            }
                                        },

                                        popupTemplate: {
                                            title: "{PlaceName}", // Data attribute names
                                            content: "{Place_addr}"
                                        }
                                    }));
                            });

                        });

                }

                // Search for places in center of map
                view.watch("stationary", function (val) {
                    if (val) {
                        findPlaces(select.value, view.center);
                    }
                });

                // Listen for category changes and find places
                select.addEventListener('change', function (event) {
                    findPlaces(event.target.value, view.center);
                });

            });
        }

        // onError Callback receives a PositionError object
        //
        function onError(error) {
            alert('code: ' + error.code + '\n' +
                'message: ' + error.message + '\n');
        }

        onDeviceReady();