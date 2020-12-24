#Errores en tiempo de ejecución

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplica(num1, num2):
    return num1*num2

def divide(num1,num2):  #Controlando excepciones
    try:
        return num1/num2
    except ZeroDivisionError as identifier:
        return "Operación erronea, no se puede dividir por cero",identifier

while True:
    try: #Controlando más excepciones
        op1=(int(input("Introduce el primer número: ")))
        op2=(int(input("Introduce el segundo número: ")))  
        break
    except ValueError as identifier:
        print("Los datos ingresados son incorrectos, intentalo de nuevo.")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
    print(suma(op1,op2))

elif operacion=="resta":
    print(resta(op1,op2))

elif operacion=="multiplica":
    print(multiplica(op1,op2))

elif operacion=="divide":
    print(divide(op1,op2))

else:
    print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")