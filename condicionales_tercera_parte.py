#El switch no es utilizado en Python

#Concatenación de condicionales

edad = 7
if 0<edad<100:
    print("Edad es correcta")
else:
    print("Edad no es correcta")

#Conectores logicos

print("Programa de becas Año 2020")
distancia_escuela = int(input("Introduce la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el n° de hermanos en el centro "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

#Ejercicio aplicando diccionarios y condicionales

print("Programa de selección de cursos 2020")

diccionario_cursos = {1:"Álgebra",2:"Física",3:"Historia",4:"Química"}
print("Los cursos disponibles son: ", diccionario_cursos)
input_valor = int(input("Digite el número del curso a seleccionar: "))

if input_valor in diccionario_cursos.keys():
    print("El curso que seleccionaste es: ",diccionario_cursos[input_valor])
else:
    print("El curso con el valor "+str(input_valor)+" no existe.")

#Las siguientes funciones permiten transformar el texto para los cases sensitive
#Permite transformar todo el texto en minúscula
texto_minuscula = "HOLA A TODOS"
print(texto_minuscula.lower())
#Permite transformar todo el texto en mayúscula
texto_minuscula = "hola a todos"
print(texto_minuscula.upper())