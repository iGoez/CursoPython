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
            chequeo = self.__chequeo_interno()

        if self.__enmarcha and chequeo:
            return "El coche está en marcha"
        
        elif self.__enmarcha and chequeo == False:
            return "Algo ha salido mal en el chequeo, no podemos arrancar"
        
        else:
            return "El coche está detenido"

    def caracteristicas(self):
        print("El coche tiene ",self.__ruedas, " ruedas. Un ancho de ",self.__anchoChasis, " y un largo de ",self.__largoChasis)

    #Encapsulamos el método para que no se pueda utlizar por fuera de la clase.
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas":
            return True
        else:
            return False

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
#print(miCoche2.__chequeo_interno()) #Si hacemos el llamado a un método encapsulado saldrá error


#Ejercicio
class Persona():
 def __init__(self):
  self.__nombre=""
  self.__sexo=""
  self.__edad=0
  self.__nacionalidad=""

 def introduce_nombre(self):
  self.__nombre=input("Introduce tu nombre, por favor: ")

 def introduce_sexo(self):
  while True:
   sexo=input("Introduce tu sexo H/M: ")
   sexo1=sexo.upper()
   if sexo1=="H":
    self.__sexo="Hombre"
    break
   elif sexo1=="M":
    self.__sexo="Mujer"
    break
   else:
    print("Datos introducidos no validos. Si eres hombre escribe una H y si eres una mujer escribe una M")

 def introduce_edad(self):
     while True:
        try:
            edad=int(input("Introduce tu edad: "))
            if edad<=0:
                raise TypeError("No se aceptan número menores o iguales a cero (0), intentelo de nuevo.")
            else:
                self.__edad=edad
                break
        except ValueError:
            print("Debes introducir números, no letras.")
        except TypeError as error:
            print(error)


 def introduce_nacionalidad(self):
  self.__nacionalidad=input("Introduce tu nacionalidad: ")
   
 def datos_Persona(self):
  print("Nombre: " + self.__nombre)
  print("Sexo: " + self.__sexo)
  print("Edad: " + str(self.__edad))
  print("Nacionalidad: " + self.__nacionalidad)
###############################################################
persona1=Persona()
persona1.introduce_nombre()
persona1.introduce_sexo()
persona1.introduce_edad()
persona1.introduce_nacionalidad()
persona1.datos_Persona()