try:
    archivo_texto=open("archivosExternos/archivo.txt", "r+")
    lista = archivo_texto.readlines()
    print(lista)
    lista.insert(1,"Nueva linea\n")
    archivo_texto.seek(0)
    archivo_texto.writelines(lista)
finally:
    archivo_texto.close()