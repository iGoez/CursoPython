#Continue: esta instrucción ignora el resto de instrucciones y salta a la siguiente iteracción del bucle.

for i in "Python":
    
    if i == "h":
        continue

    print(f"la letra es {i}")

#Ejercicio

texto = input("Ingrese un texto: ")
contador = 0

for i in texto:
    
    if i == " ":
        continue
    
    contador = contador+1

print(f"El total de caracteres en el texto son: {contador}")

#Pass: pasar algo por alto

for i in "hola":
    pass

#Else para bucles

for i in [5,6,7,5,5,6]:
    if i == 0:
        print(i)
        
else:   #Solo se entrará al else si no se cumple la condición del bucle
    print(i)