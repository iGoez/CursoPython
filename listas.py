numeros = [1,2,3,4,5] # Sintaxis de las listas

#las listas pueden tener diferentes tipos de elementos.

print(numeros[:]) # Toma todos los elementos de la lista

print(numeros[0:3]) # Imprimir hasta ciertos elementos. el 0 lo toma y el 3 no.

print(numeros[:3]) # [X:Y] si X no tiene un valor se tomará como un 0. En caso contrario
print(numeros[0:]) #si Y no tiene valor entonces se tomará hasta el final del arreglo.

numeros.append(6) #Sirve para agregar elementos a la lista, se agregan en la última posición.
numeros.insert(1,9) #Sirve para agregar un elemento en una ubicación en especifico de la lista.

numeros.extend([10,11,12]) #Sirve para agregar varios elementos a una lista

print(numeros.index(10)) #Sirve para saber la posición de un elemento en la lista. 

print(numeros[2]) #Obtener un valor de la lista

print(5 in numeros) #el in funciona para saber si el elemento se enuentra en la lista
print(20 in numeros)

numeros.remove(5) #Sirve para eliminar elementos de la lista
numeros.pop() #Sirve para eliminar el último objeto de la lista

#Se pueden concatenar listas
miLista2 = ["Iván Camilo"]
miLista3 = ["Goez Palacio"]
miListaResultado = miLista2+miLista3 #Con el signo de + se pueden concatenar listas

print(miListaResultado*3) #Sirve para repetir varias veces la lista

for j in miListaResultado:
    print(j, end=', ')

print("\n")

for i in numeros:
    print(i, end=', ')