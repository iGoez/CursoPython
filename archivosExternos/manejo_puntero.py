# Vamos a situar el puntero en algún lugar del texto
# La instrucción seek() nos ayuda a ubicarnos. Recibe un parametro donde colocamos el numero del caracter donde queremos empezar. 
archivo_texto=open("archivosExternos/archivo.txt", "r")

texto = archivo_texto.read()
print(texto)

#Aquí me ubico en el principio del texto
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.read())/2)

# El comando read también puede recibir un parametro de donde queremos terminar de leer el texto
texto = archivo_texto.read()
print(texto)

archivo_texto.close()

# Podemos hacer lectura y escritura de una vez colocan r+
archivo_texto=open("archivosExternos/archivo.txt", "r")
lista = archivo_texto.readlines()
print(lista)
archivo_texto.close()

lista.insert(2,"Agregando una nueva linea con el readlines y el writelines\n")

archivo_texto=open("archivosExternos/archivo.txt", "w")
for i in lista:
    archivo_texto.write(str(i))
archivo_texto.close()