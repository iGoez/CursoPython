import math


#La instrucción Raise permite lanzar excepciones
def evaluaEdad(edad):
    if edad<0:
        raise TypeError("No se permiten edades negativas") #TypeError (o cualquier error) y el respectivo mensaje de error que queremos que muestre.
    elif edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate..."

while True:
    try:
        print(evaluaEdad(int(input("Ingrese su edad: "))))
        break
    except TypeError as identifier:
        print(identifier, "intentelo otra vez")

#Otro ejercicio
#Para que el programa siga su ejecución se debe capturar la excepción

def calcularRaiz(numero:int):
    if numero<0:
        raise ValueError("El número ingresado no puede ser negativo")
    else:
        return math.sqrt(numero)

while True:
    try:
        print(calcularRaiz(int(input("Ingrese el número: "))))
        break
    except ValueError as identifier:
        print(identifier, "intentelo otra vez")