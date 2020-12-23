#Los diccionarios son como los hashmap, son de la forma clave:valor
#Permiten guardar todo tipo de objetos

#Sintaxis del diccionario
miDiccionario = {"Colombia":"Cali", "España":"Madrid", "Japon":"Tokio"}
print(miDiccionario)

#Para consultar en el diccionario se escribe la llave del valor
print(miDiccionario["Colombia"])
print(miDiccionario["Japon"])

#Agregar un elemento al diccionario
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)

#Si el elemento ya existe, lo va a sobreescribir.
#Sirve también para cambiar el valor de una llave
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

#Sirve para eliminar un elemento del diccionario
del miDiccionario["España"]
print(miDiccionario)

#Guardando una tupla y utilizando los valores
miTupla = ("España", "Francia", "Reino Unido", "Alemania")
nuevoDiccionario = {miTupla[0]:"Madrid", miTupla[1]:"París", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
#Se puede acceder al diccionario de las dos formas
print(nuevoDiccionario["Francia"])
print(nuevoDiccionario[miTupla[1]])

#Agregando una tupla en el diccionario
otroDiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1997,1998]}
print(otroDiccionario)
print(otroDiccionario["anillos"])
#Aquí ya puedo interactuar con la tupla una vez obteniendola con la llave
otroDiccionario["anillos"].append(2000)
print(otroDiccionario)
otroDiccionario["anillos"].remove(2000)
print(otroDiccionario)

#Interactuando con un diccionario dentro de otro
newDiccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1997,1998]}}
print(newDiccionario.keys())
print(newDiccionario.values())
#Forma de obtene un valor de lista que esta contenida en un diccionario, a la vez que éste está contenido en otro diccionario 
print(newDiccionario["anillos"]["temporadas"][4])