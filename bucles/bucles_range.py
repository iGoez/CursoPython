#Recorriendo una lista
for i in ["Pildoras", "Informaticas", 3]:
    print(i, end=", ")  #el end permite que se imprima en una sola línea

#Recorriendo un String
for i in "Camilo Goez":
    if i != " ":
        print(i, end=" ")

print("\n")

#Utilizando el range
#range(x,y) donde x es el parametro donde se empieza y y donde termina, si no se coloca x entonces empieza en 0
#En el caso de y, es obligatorio y no lo incluye
for i in range(10):
    print(i,end=" ")

#Caracteres especiales en el print
for i in range(11):
    print(f"Valor de la variable {i}")  #El caracter f me permite unir una variable con textos

#El range tiene un tercer argumento que permite movernos de x en x
for i in range(5,20,2):
    print(i)

#Ejercicio: saber si un caracter está en una entrada de texto

email = input("Ingrese su correo eléctronico: ")

for i in range(len(email)):
    if email[i] == "@":
        print("valido")