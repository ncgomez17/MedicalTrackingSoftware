# MedicalTrackingSoftware
Proyecto ALS: Medical Tracking Software
Nicolás Cid Gómez    

Esta aplicación está dirigida a las personas que trabajan en el ámbito médico y tienen una consulta.Les permitirá gestionar registros médicos, medicamentos y diagnósticos de los pacientes que tenga cada usuario.A mayores, proporciona el servicio de localización de hospitales, clínicas y farmacias cercanas para poder recomendar a los pacientes lugares donde poder pillar medicamentos o realizar los tratamientos.
En cuento a la gestión de registros,medicamentos y diagnósticos, los usuarios podrán añadir,editar,borrar,buscar y visualizar estos.

Descripción técnica:

En cuanto a las tecnologías usadas en este proyecto están:
1.	Python 2.7
2.	GAE(Google Aplication Engine)
3.	Javascript
4.	Tailwind CSS
En cuanto a la distribución del proyecto, este se ha dividido en varias carpetas para poder diferenciar cada una asignándole unas determinadas responsabilidades:
5.	assets:En esta carpeta se encontrarán otras carpetas que guardarán imágenes de distintos tipos, así como iconos,imágenes vectoriales,etc …
6.	CSS:Se guardarán los ficheros con las propiedades CSS
7.	handlers: Esta carpeta esta divida en otras 3 carpetas que pertenecen a las distintas entidades del proyecto.En esta carpeta se crearán los distintos archivos que nos permitirán manejar las peticiones que se hagan en las distintas rutas que tenemos declaradas.
8.	JS:Se guardarán todos lo archivos javascript del  proyecto.
9.	Model:Se guarda la especificación de los atributos de cada entidad.
10.	templates:Aquí se encuentran las distintas plantillas HTML5.
11.	Utils:En esta se crean archivos auxiliares que permitirán propocionar nuevas funcionalidades a otras carpetas como la de handlers.
En el directorio raíz se encuentra el archivo app.yaml en el que se guardarán las distintas configuraciones del proyecto,indicando las dependencias de librerías,carpetas que contiene este y rutas especificadas.

Funcionalidades:

1.	El tema de la localización de los distintos lugares se lleva a cabo con JavaScript en concreto el archivo index.js
2.	Los archivos que se encargan de las gestión de cada entidad se encuentran en la carpeta handlers,dentro de una carpeta con el nombre de la entidad.

Se ha realizado herencia de plantillas con JINJA2, la plantilla base del proyecto es index.html, las demás heredarán está y la modificarán correspondientemente.
Para la creación de las tablas y de los formularios también se ha usado JINJA2 que nos permitirá hacer bucles y coger los campos de las distintas entidades que devuelvan las peticiones.
Se han realizado comprobaciones básicas en las plantillas html pero también se realizan validaciones en JavaScript en el fichero comprobaciones.js.
Por último mencionar que también se gestiona un registro de usuarios mediante correo electrónico, así podemos relacionar las distintas entidades con el usuario que las haya creado.
