# Postgres
Para este proyecto necesitamos utilizar el gesto de base de datos **Postgres**. Primero vamos a instalar Postgres de la siguiente maneja, abrimos una terminal  colocamos:
>sudo apt-get install postgresql-server-dev-9.x

Para entrar a Postgres desde el terminal tenemos que digitar el siguiente comando:
>sudo -i -u postgres

Ahora vamos a iniciar el cliente de **psql** para poder escribir nuestro código Sql:
>psql

Para crear nuestra base de datos, lo hacemos con el siguiente código:
>create database base_practica with owner=usuario;

Para salirnos del cliente **psql** y de Postgres digitamos lo siguiente:
>\q

>exit

Finalmente cuando ya tengamos todo nuestra base de datos en un archivo *.sql lo siguiente que tenemos que hacer es migrar todo el codigo a Postgres para que se organicen todos los datos, para esto tenemos que digitar en una terminal lo siguiente:
>psql -U postgres -W -h localhost base_practica < archivo.sql


# Usando Django
Django es un framework de desarrollo Web , este se enfoca en el modelo **mvt** donde se distinguen los siguientes archivos : **models.py** ,**views.py** ,**urls.py** y el **index.html**; estos 4 tipos de archivos python son la parte principal donde cada uno realiza una parte esencial como por ejemplo:
###models.py
Contiene una descripción de la tabla de la base de datos , donde también podemos editar los distintos elementos que posee (usando cóigo python , no 'SQL')
###views.py
Contiene la lógica de la página, donde declaramos nuestras vistas y donde le vamos a decir que tiene que hacer y que retorna
###index.html
No precisamente este archivo html se va a llamar 'index', puede tener cualquier nombre , en este archivo lo vamos a utilizar para hacer el diseño de nuestras plantillas , donde usaremos declaraciones que interprete Django

# Instalando Django:
Django esta escrito en código python por lo tanto tenemos que instalar la versión 2 o 3 de este mismo, por lo general en linux 'Ubuntu' ya llega instalado alguna versión pero para constatar que tenemos una abrimos una terminal y procedemos a digitar lo siquiente: **Python 2.7** o  **Python3** y nos aparecera algo como esto:
>Python 3.5.2 (default, Aug  8 2016, 10:57:32) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.

O si queremos alguna otra versión descargamos la que queramos de la página oficial aquí: [Descarga python](https://www.python.org/downloads) .Luego de descargarlo instalamos manualmente el archivo **.tar** 

Seguidamente tenemos que hacer un **update** para tener actualizados los repositorios de nuestro sistemas, asi que en una terminal digitamos : 
>sudo apt-get update

Luego instalamos todos los paquetes necesarios de python ,para esto digitamos en la terminal:
>sudo apt-get install python-dev
sudo apt-get install python-setuptools

Una característica de Django es que llega con una base de datos por defecto (sqlite). Pero nosotros vamos a trabajar con el gestor de base de datos **Postgres** el cual ya lo instalamos anteriormente

Ahora necesitamos instalar un entorno virtual para poder manejar nuestros proyectos independientemente uno del otro para no generar conflicto entre  versiónes. 
Cuando instalamos el paquete **python-setuptools** este nos da la opción de usar el  **easy_install** , el cual nos permite instalar facilmente los paquetes que necesitemos ;ahora con este comando vamos a instalar los paquetes necesarios para que funcione nuestro entorno virtual, asi que vamos a la terminal y digitamos:
>sudo easy_install virtualenv

Ahora que tenemos todos los paquetes necesarios para nuestro entorno virtual procedemos a crear uno ,que en este caso se va a llamar "entorno_demo", digitamos en la terminal:
>virrtualenv /ruta_del_entorno/entorno_demo

Luego que tenemos nuestro entorno virtual procedemos a activarlo, de la siguiente manera:
Primero , entramos a la carpeta que se nos creó (entorno_demo):
>cd /ruta_del_entorno/entorno_demo

Segundo ,procedemos a la activación con la siguiente linea:
>source /ruta/del/entorno/entorno_demo/bin/activate

Ahora que ya estamos dentro del entorno ,tenemos que instalar una libreria de Postgres para Python ,y asi poder sincronizar todo correctamente con la base de datos, así que en la terminal digitamos el siguiente comando:
>pip install psycopg2

( **pip** ya está instalado si estamos utilizando Python2 o Python3, también se instalará si estamos trabajando en un entorno virtual )

Ahora si vamos a instalar Django, solo tenemos que digitar en la terminal lo siquiente:
>pip install django

Si queremos una versión especifica solo tenemos colocar luego de la palabra django un **==** y seguido de esto la versión ,de este modo:
>pip install django==1.8

Teniendo Django instalado vamos a crear nuestro proyecto ,para esto nos situamos en la ruta donde queramos que vaya el proyecto y digitamos en la terminal lo siguiente:
>django-admin.py startproject transito 

Suponiendo que tenemos todo configurado y que esta en marcha nuestra base de datos (en Postgres) vamos a configurar 
un archivo que se crea a lo que iniciamos nuestro nuevo proyecto ,este es el archivo llamado **settings.py** ,lo abrimos y colocamos lo siguien:
 ``` [language]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Ejemplo_DB',
        'USER': 'Ejemplo_Usuario',
        'PASSWORD': 'password_usuario',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
 
 ```
Ahora vamos a crear una aplicación para hacer funcionar todo , para esto nos vamos a la ruta que deseemos y digitamos esto en la terminal:
>python manage.py startapp app1

En este punto ,solo nos falta el modelo de la base de datos en python  para que el administrador de Django pueda interpretar los datos , para eso tenemos que digitar el siguiente comando en la terminal:
>python manage.py inspectdb > mysite/myapp/models.py

este **inspectdb** lo que hace es determinar una representación del modelo que usara Django para cada una de las tablas de la base de datos y luego transforma todo eso en código Python ,finalmente nos crea un archivo **models.py** donde está todo el código generado en la ruta donde se indica en el comando.
De esta manera trabaja el **inspectdb**:
``` [language]
class Clasevehiculo(models.Model):
    descripcion = models.CharField(max_length=60, blank=True, null=True)
    idclasev = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'clasevehiculo'
	verbose_name = u'Clase de vehiculo'
        verbose_name_plural = u'Clase de vehiculos'
    def __unicode__(self):
return self.descripcion

```

Como hemos generado el modelo dentro de la aplicacion solo tenemos que migrar todos los datos para que podamos ver los cambios. Para migrar los datos se digita lo siguiente:
>python manage.py makemigrations

>python manage.py migrate

finalmente para acceder al admin de Django y ver los cambios que hemos realizado ,tenemos que crear un super usuario y lo creamos de la siguiente manera en la terminal:
>python manage.py createsuperuser

Ahora si podemos ver lo que hemos hecho ,así que tenemos que correr el servidor y entrar a un navegador web en la siguiente [url](https://127.0.0.1:8000/admin) y para correr el servidor digitamos lo siguiente en la terminal:
>python manage.py runserver

Finalmete si queremos visualizar los datos fuera del admin de Django tenemos que configurar  las vistas y las url's , también podemos incluir plantillas para que nuestro trabajo se vea más estilizado.
