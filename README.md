# Tercera-preentrega-Tapia-Agustin


|Inicié el proyecto comenzando con el codigo| "django-admin startproject <nombre del proyecto> ", donde cree mis views y plantillas.

◄ 3 Modelos donde se encontrará un formulario en c/u en el SITIO WEB.

-----<Formulario: Precio y Cantidad.>   

◄ Los articulos creados son: <Silla, Sillon y Mesa.> ◄ 

◄ Modelo:"<Silla>"
----> Se permitira filtrar los resultados que escribimos en el formulario previo. <-----
<views.busquedaSilla> ---- <views.buscar_silla>

* - Cada informacion que agreguemos en estos, 
se guardarán en la base de datos del Admin.

◄ Aplicación creada con el comando "python manage.py startapp <nombre del app>"

◄ Para actualizar la base de datos del proyecto con cambios en nuestros modelos:
    2 PASOS:
    <python manage.py makemigrations>
    <python manage.py migrate>

python manage.py migrate

Crear la siguiente estructura de carpetas: ejemplo/templates/ejemplo

Dentro de la carpeta ejemplo/templates/ejemplo crear el archivo saludar.html y agregar el codigo
