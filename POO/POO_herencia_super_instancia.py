class Persona():

    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia=lugarResidencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ",self.edad, " Lugar de Residencia: ",self.lugarResidencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado,edad_empleado,residencia_empleado):

        #Forma de llamar el constructor del padre
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)

        self.salario = salario
        self.antiguedad = antiguedad
    
    #Como vamos a sobrescribir el método de la clase padre entonces hacemos el super() para llamar su antiguo contenido
    def descripcion(self):
        #Está es la forma de llamar a un método de la clase Padre si vamos a sobreescribir el método
        super().descripcion()
        print("Salario: ", self.salario, " Antiguedad: ",self.antiguedad)

empleado = Empleado(1000,5,"Camilo",55,"Colombia")
empleado.descripcion()

#Principio de sustutición: X siempre es una Y (Nuestro ejemplo sería la clase Empleado es siempre una clase Persona
#Se utiliza este principio para saber si un diseño de herencia es correcto

#isInstance se utliza para saber si una clase es una instancia de otra
#Es este caso, empleado es instancia de empleado my persona porque la clase Empleado hereda de Persona
print(isinstance(empleado,Empleado))