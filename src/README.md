Descargar Python 2.7.18

-Al tener instalado Python se tiene que acceder a la carpeta dónde se guardó en este caso en el disco local C, despues encontrar la carpeta python 27, y copiar Python y Pythonw a la carpeta de Scripts al hacer todo ese procedimiento en la misma instancia de la busqueda de carpetas, nos vamos a la CMD en donde tenemos que anotar unos comandos para instalar unos paquetes:
1.- pip install colorama
2.- pip install socks
3.- pip install requests
4.- pip install modules
5.- pip install bs4


Intalación del entorno virtual

-Ahora instalaremos el entorno virtual, en la cuál no se reconocía el termino "virtualenv" entonces se buscó una solución para que pueda crearse el entorno viertual y la solución fué ver en la cmd y colocar en la terminal:
"python --version" para ver la versión de python instalada y "pip --version" para ver la versión del pip (Package Installer Python) al tener todo correcto con la información, anotamos "pip list" para ver si tenemos el virtualenv a la cuál no la tengo instalada, entonces se tiene que instalar en la terminal de manera global, para ello utilizaremos el comando de "pip install virtualenv".

-Al terner el virtualenv, nos vamos al terminal de visual studio para proceder a la activación del entorno virtual, en la cuál se utilizará el comando "virtualenv -p python2.7.18 venv-python3" para tener el entorno virtual creado en dónde se crean otras carpetas del entorno virtual como: Lib, Scripts, .gitignore y pyvenv.cfg.
Entonces se activa el entorno virtual con el comando de enrutamiento ".\env\Scripts\activate".

-Actualizaremos el pip en la terminal de visual studio para no terner futuros problemas.

-Se hace la prueba de instalar carpetas como Flask y Django en el entorno virtual.

-Se crea una carpeta src para hacer las pruebas de hacer correr lo que se está desarrollando.

-Ahora se exportarán los paquetes que se tienen con el comando "pip freeze > requirements.txt" en la cuál se ven todos los paquetes que se tienen instalados en este caso se hace en el cuál se realiza un proyecto y se requiere migrarlo a otra computadora. 

-Y para desactivar el entorno virtual se utiliza el comando "deactivate".


Instalación MongoDB

-Al instalar MongoDB nos dirigimos a la CMD y se ejecutará el comando "mongod.exe --version" en donde no se reconoce el programa ejecutable, entonces nos dirigimos a un explorador de archivos y buscamos las carpetas: program files, MongoDB, Server, 7.0, bin y se copia toda la ruta en la busqueda de carpetas en dónde tenemos que añadir a las variables de entorno y nos dirigimos a las propiedades del disco local C, configuraqción avanzada del sistema y agragamos el enrutamiento en el path de la variable de entorno y volvemos a colocar el comando "mongod" para dejar la base de datos corriendo, pero sale otro error ya que el directoria de la data no ha sido encontrado en la cuál debemos crear una carpeta llamada "data" y desntro de ella cramos una carpeta llamada "DB" para que mongoDB deposite los archivos propios del servidor y se soluciona el problema.

-Ahora se instalará mongoDB shell y se abre otra terminal para que escuche una conexión, en la cuál se coloca un comando "mongosh" para que corra en un local host en el puerto 27017 que es el mismo puerto del mongoDB estaba esperando predeterminadamente.



Conexión Python con MongoDB

-Para conectarnos a MongoDB necesitamos un paquete en la cuál se instala abriendo la terminal de visual studio colocando el comando "pip install pymongo" y para ver que está funcionando, tendremos que correr el programa de mongoDB colocando en la terminal "mongod" para iniciar la conexión. 
Nos conectamos al local host del programa mongoDB y se crea una nueva base de datos, después nos dirigimos a visual studio en donde haremos la conexión con mongoDB en dónde tendremos que importar pymongo y el siguiente código
"client = pymongo.MongoClient("mongodb://localhost:27017/mi_base_de_datos")
db = client["mi_base_de_datos"]
collection = db["mis_pedidos"]"
y ya estará conectada el pymongo.


CRUD

-Lo que hace el CRUD es un pedido en dónde el que está tomando la orden, registra el nombre del cliente, la comida pedida y el precio a pagar y aquello se queda registrado en la base de datos.
También puede eliminar, modificar, actualizar y ver el pedido registrando colocando el nombre del cliente.
