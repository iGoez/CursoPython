#Primeros pasos de Python
#Funciones

def mensaje():
    print("Hola mundo")
    print("Primeros pasos de Python")

mensaje()

def suma(num1, num2):
    print(num1+num2)

suma(5,5)

def suma2(num1, num2):
    return num1+num2

print(suma2(10,10))

almacenar_valor=suma2(10,10)+50

print(almacenar_valor)