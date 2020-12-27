# Open() pide dos parametros, el nombre del archivo para abrir/crear y el modo (lectura, escritura o append)
#append: agregar texto a un archivo existente
# Escritura = "w"
# Lectura = "r"
# Append = "a"

# Las cuatro fases: crear, abrir, modificar y cerrar

# Open() pertenece a io, no lo importamos porque lo reconoce por defecto

archivo_texto=open("archivosExternos/archivo.txt", "w")

frase= "Probando los archivos externos \nHoy es 27/12/0020"

#Para escribir en el archivo utilizamos el write
archivo_texto.write(frase)

#Tenemos que terminar con su última fase, es por esto que cerramos el archivo dque abrimos desde memoria
archivo_texto.close()

########### Ahora vamos a abrir el archivo en modo lectura y obtener su información ################

archivo_texto=open("archivosExternos/archivo.txt", "r")

# Nos permite obtener toda la información del archivo
texto = archivo_texto.read()
print(texto)

# También podemos leer linea por linea y guardarla en una lista
# listaTexto = archivo_texto.readlines()
# print(listaTexto[])

archivo_texto.close()

########### Ahora vamos a abrir el archivo en modo append y agregar más información ################

archivo_texto=open("archivosExternos/archivo.txt", "a")

#Para escribir en el archivo utilizamos el write
archivo_texto.write("\nAgregando una nueva linea con el append")

#Tenemos que terminar con su última fase, es por esto que cerramos el archivo dque abrimos desde memoria
archivo_texto.close()