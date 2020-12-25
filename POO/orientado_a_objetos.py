#Conceptos

# Clase: Modelo donde se redactan las características comunes de un grupo de objetos
# Instancia: Ejemplar perteneciente a una clase
# Modularización: Sus clases son indepedientes, se pueden reutilizar en otros programas.
# Encapsulación: Proteger las propiedad de una clase y no se puedan modificar desde afuera
# Métodos de acceso: Permiten conectar entre clases.

class Coche():
    #Estás variables son un estado inicial nominado constructor
    #__init__ es el constructor en Python
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4 #Los dos guiones se utilizan para encapsular una propiedad
        self.__enmarcha=False

    #El def debe ser un método de la clase más no una función
    #El parametro self hace referencia al objeto perteneciente a la clase
    #el self es igual al this de JAVA, pero en Python es obligatorio colocarlo
    def arrancar(self, enmarcha):
        self.__enmarcha = enmarcha

        if self.__enmarcha:
            return "El coche está en marcha"
        else:
            return "El coche está detenido"

    def caracteristicas(self):
        print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ",self.__anchoChasis, " y un largo de ",self.__largoChasis)


#Instanciar una clase (objeto)
#No se utiliza en new como en JAVA
miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.caracteristicas()

#Creando el segundo objeto

print("--------------Creando el segundo objeto--------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2 #Aquí un ejemplo de que no podemos cambiar el valor de una propiedad encapsulada si esta se encuentra fuera de la clase
miCoche2.caracteristicas()
