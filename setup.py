from setuptools import setup

# Aquí se coloca todas las configuraciones de nuestro paquete
setup(
    name="PaqueteCalculos",
    version="1.0",   #Aquí se coloca la versión por si más adelante se actualiza el módulo que vamos a distribuir
    description="Paquete de dividir y multiplicar", #Descripción de nuestro módulo
    author="Camilo",
    author_email="ejemplo@hotmail.com",
    url="www.cualquierCosa.com",
    packages=["paquetes", "paquetes.paquetes_modulos","paquetes.paquetes_modulos.operaciones_basicas"] #Obligatorio, donde se encuentra el paquete o subpaquetes que vamos a distribuir
)

