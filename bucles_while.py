import math

#Sintaxis de while
i = 0
while i <= 10:
    print(i)
    i = i+1

#Ejercicio: Ingresar la edad por teclado
edad = int(input("Ingrese la edad: "))

while edad<0:
    print("La edad es negativa")
    edad = int(input("Ingrese la edad: "))

print(f"Su edad es {edad}")

#Raíz cuadrada de un número
print("Programa para calcular la raíz de un número")

intentos = 3
numero = int(input("Ingrese el número: "))

while numero<0:
    print("El número ingresado es menor que cero (0)")
    numero = int(input("Ingrese el número: "))
    intentos = intentos-1
    if intentos == 0:
        print("Intentos terminados")
        break   #El break me permite salir del bucle y continuar la ejecución de las líneas siguientes.
    else:
        print(f"Te quedan {intentos} intentos.")

if numero>=0:
    print(f"El resultado es: {math.sqrt(numero)}")