print("Programa de evaluación de notas de alumnos")

#Los valores del input siempre son string/str
nota_alumno = int(input("Introducir nota del alumno: "));

#Condicional if
def evaluacion(nota):
    valoracion = "Aprobado"
    if nota<5:
        valoracion = "No aprobado"
    return valoracion

print(evaluacion(nota_alumno))