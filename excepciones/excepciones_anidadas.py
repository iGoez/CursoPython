#Ejercicios: excepciones anidadas
def divide():
    
    try:
        op1 = float(input("Ingrese el primer número: "))
        op2 = float(input("Ingrese el segundo número: "))

        print("La división es ",str(op1/op2))
    except ZeroDivisionError:
        print("Error al dividir por cero (0)")
    except ValueError:
        print("Campos ingresados erróneos")
    #La instrucción finally se utiliza en las bases de datos para cerrar si o sí la conexión de la base
    finally:
        print("Cálculo finalizado") #Finally se ejecuta siempre

divide()