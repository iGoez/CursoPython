#Sintaxis de una tupla. Los paréntesis no son obligatorios.
#Igual que las listas, las tuplas pueden tener diferentes tipos de elementos.
nombreTupla = (1,2,3,4,5,"Hola")
print(nombreTupla)

#Convertir una tupla en una lista
nombreLista = list(nombreTupla)
print(nombreLista)

#Convertir lista a tupla
nuevaTupla = tuple(nombreLista)
print(nuevaTupla)

#Saber si un elemento está o no contenido
print(5 in nombreTupla)
print(6 in nombreTupla)

#Saber la cantidad de un mismo valor en la tupla
print(nombreLista.count(5))
print(nombreTupla.count(5))

#Saber el tamaño de una lista/tupla
print("Cantidad de tupla: "+str(len(nombreTupla)))
print("Cantidad de la lista: "+str(len(nombreLista)))

#Tupla unitaria
tuplaUnitaria = ("Hola",) #La coma , es necesaria para referirse que la tupla es unitaria
print(tuplaUnitaria)

#Desempaquetar tuplas
miTupla = ("Iván","Camilo","Goez","Palacio")
pNombre, sNombre, pApellido, sApellido = miTupla
print(pNombre)
print(sNombre)
print(pApellido)
print(sApellido)

#Sirve para conocer la posición de un elemento
print(miTupla.index("Iván"))