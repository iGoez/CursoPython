# Ejercicio 1
# Realizar un programa que conste de una clase llamada Alumno
# que tenga como atributos el nombre y la nota del alumno.
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
# un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():

    def __init__(self,nombre,nota):
        self.__nombre = nombre
        self.__nota = nota
    
    def __str__(self):
       return "Nombre del alumno: {} \nNota del alumno {}".format(self.__nombre,self.__nota)

    def calificacion(self):
        return "Aprobado" if self.__nota>=3 else "No aprobado"


miAlumno = Alumno("Camilo", 4)
print(miAlumno)
print(miAlumno.calificacion())

# Ejercicio 3
# Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos,
# imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo():

    def __init__(self, ladoUno, ladoDos, ladoTres):
        self.ladoUno = ladoUno
        self.ladoDos = ladoDos
        self.ladoTres = ladoTres
    
    def tamanioMayor(self):
        mayor = 0
        if self.ladoUno >= self.ladoDos and self.ladoUno>=self.ladoTres:
            mayor = self.ladoUno
        elif self.ladoDos>=self.ladoTres:
            mayor = self.ladoDos
        else:
            mayor = self.ladoTres
        return "El lado mayor es: {} cm".format(mayor)

    def tipoTriangulo(self):
        texto = ""
        if self.ladoUno == self.ladoDos and self.ladoUno == self.ladoTres:
            texto = "El triangulo es equilátero"
        elif self.ladoUno == self.ladoDos or self.ladoUno == self.ladoTres or self.ladoDos==self.ladoTres:
            texto = "El triangulo es isósceles"
        else:
            texto = "El triangulo es escaleno"
        return texto

miTriangulo = Triangulo(80,70,90)
print(miTriangulo.tamanioMayor())
print(miTriangulo.tipoTriangulo())