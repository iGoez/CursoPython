# Los paquetes distribuibles sirven para reutlizar el código de los módulos en otros proyectos.


# Se debe crear un nuevo archivo que se llama setup.py
# El archivo contendrá la configuración del paquete distribuible
# El setup.py se crea en la raíz de la carpeta

# from setuptools import setup
#
# setup(
#     name="NombrePaquete", #El nombre que le queramos colocar al paquete
#     version="v1",   #Aquí se coloca la versión por si más adelante se actualiza el módulo que vamos a distribuir
#     description="Descripción", #Descripción de nuestro módulo
#     author="Camilo",
#     author_email="ejemplo@hotmail.com",
#     url="www.cualquierCosa.com",
#     packages=["paquetes","paquetes.paquetes_modulos","paquetes.paquetes_modulos.operaciones_avanzadas"] #Obligatorio, donde se encuentra el paquete o subpaquetes que vamos a distribuir
# )

# 
# Después de configurar el setup se debe escribir python setup.py sdist para crear nuestro archivo distribuible
# Después de la instrucción se crearán dos carpetas llamadas dist y otro archivo con el nombre que colocamos en el setup

# Ahorta vamos a instalar el paquete, tenemos que dirigirnos a la carpeta donde está el paquete (dist) desde consola y escribir la siguiente instrucción
# pip3 install nombrePaquete
# Una vez instalado ya podemos utilizar nuestro archivo y ejecutarlo en cualquier lado del ordenador