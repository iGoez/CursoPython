# Para hacer uso de funciones de otros archivo hay que importar la clase
# Aquí importamos todas las funciones y nos tocaría usar modulos.Nombrefuncion para utilizar la funcion

# import modulos

# No solo basta importar, sino que utilizar el nombre del archivo
# modulos.suma(5,5)
# modulos.resta(5,5)

# Podemos utilizar lo siguiente para importar solamente una función en especifico
from modulos import suma
from modulos import resta

#Por otra parte, si queremos importar todo sin necesidad de utilizar el llamado con el modulo entonces:
# from modulos import *
#Es mejor utilizar importar una función en especifico para no reservar memoria

print(suma(5,5))
print(resta(5, 5))
