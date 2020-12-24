#Son estructuras que extraen valores de una función
#y se almacenan en objetos iterables (que se pueden recorrer).

#Los generadores nos devuelven valor por valor, hay que hacer varios llamados.

#Ejercicio
#Método sin generador
def generarPares(longitud):
    num = 1
    lista = []
    while num<longitud:
        lista.append(num*2)
        num = num+1
    
    return lista

print(generarPares(10))

#Método con generador
def generarParesConGenerador(longitud):
    num = 1
    while num<longitud:
        yield num*2
        num = num+1

obtenerPares = generarParesConGenerador(10) #Aquí permanece en reposo porque no se ha llamado la función

print(next(obtenerPares))

for i in obtenerPares:
    print(i, end=" ")