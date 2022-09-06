Pagina para administradorass de  “Tienda Olivia” - emprendimiento de sublimado, que busca reinventar objetos de la vida cotidiana con un diseño adaptable a cada persona. 

Al ingresar a http://127.0.0.1:8000/ podemos visualizar una pagina de bienvenida general

Al ingresar a "Productos", podremos observar un listado de los productos que comercializa Tienda Olivia, con las respectivas acciones que puede realizar el empleado.

Para editar, borrar o actualizar la información de un producto, el usuario debe estar logueado, dirigiéndose al botón "Iniciar secion".

Si es la primera vez que una administradora ingresa a la pagina, deberá registrarse, completando su nombre, email, y contraseña. Al registrarse, debera cargar una foto de avatar que lo represente. 

En la pagina principal,  contamos con un buscador para localizar mas rápido el producto deseado.

A su vez, navegando por las distintas solapas de la Web, se podrá encontrar informacion sobre las sucursales y sobre los integrantes del equipo.

Contamos tambien, dentro de la solapa "Mi Perfil", con distintas acciones que puede realizar el usuario, entre ellas, el envio de un Mensaje a otro usuario.

Si se desea ingresar a la base de datos con usuario administrador, se debe hacer a traves de : http://127.0.0.1:8000/admin

Division de las tareas:

El montado de la pagina fue realizado por Guadalupe Romero y Camila Pedulla, detallando a continuación las tareas realizadas por cada una:

-Guadalupe Romero: Editar los usuarios, Crear avatar, Cargar avatar, Mensajeria.
Armado de la APP "Mensajes", desarrollando las funciones necesarias para el envio y recepcion de mensajes entre los perfiles. En la APP log web, realizamos el armado de una funcion que permite cargar el avatar de un perfil, cargando una imagen.

-Camila Pedulla: CRUD Productos, Log in, Registrar usuario, Log out.
Armado de la APP log web, desarrollando las funciones necesarias para poder realizar el inicio de sesion de un usuario, su registro en el sistema, y la salida del mismo. En la APP Web Page, realizamos el armado de un CRUD que permite editar, borrar y actualizar los productos.


Detallamos a continuacion lo necesario para poder ver nuestra Web en funcionamiento:


1.	Clonar el proyecto
2.	Instalar las dependencias del proyecto: pip install django
2.	Instalar las dependencias del proyecto: pip install Pillow
3.	Crear las migraciones ejecutando python manage.py makemigrations y luego python manage.py migrate
4.	Correr la aplicacion con python manage.py runserver


Podran acceder a los casos de prueba desde el siguiente link:

https://docs.google.com/document/d/1V-peiQur3BmYyDqB4pSWkc0gVemZ-tsFz05B_5XJ3nA/edit


Video demostrativo:
https://www.loom.com/share/5d1bdf3fb5bc4d92a78b13442a2a5d22
