#Simplificar el código de los generadores en el caso de utilizar bucles anidados

#Método sin el yield from
def devuelve_ciudades(*ciudades): #el * se refiere a que se va a recibir un número indeterminado de objetos. También que se van a recibir en forma de tupla
    for elemento in ciudades:
            for elem in elemento:
                yield elem

ciudades = devuelve_ciudades("Cali", "Medellin", "Bogotá", "Barranquilla")

#Método con el yield from
def devuelve_ciudades_yieldFrom(*ciudades): #el * se refiere a que se va a recibir un número indeterminado de objetos. También que se van a recibir en forma de tupla
    for elemento in ciudades:
            #for elem in elemento:
                yield from elemento #Hacer un yield desde elemento, esto nos ahorra el recorrido del segundo for