print("Continuación de la segunda parte de los condicionales")

texto_entrada = int(input("ingrese la nota del alumno: "))

if texto_entrada < 3:
    print("No aprobado")
elif texto_entrada == 3:
    print("En valoración")
else:
    print("Aprobado")