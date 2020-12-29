import pickle

lista_nombres = ["Pedro", "Ana","María"]

# Serialización guarda el archivo en binario por ende necesitamos escribir nuestro archivo en binario con wb
fichero_externo = open("serializacion/listaNombres","wb")

# Aquí hacemos el volcado de datos
pickle.dump(lista_nombres, fichero_externo)

fichero_externo.close()

# Lo borramos de memoría
del(fichero_externo)


# Ahora procedemos a abrir el archivo binario #

# Lo abrimos en modo lectura de binario rb
fichero_externo = open("serializacion/listaNombres","rb")

# y cargamos los datos 
lista = pickle.load(fichero_externo)

print(lista)
fichero_externo.close()
del(fichero_externo)