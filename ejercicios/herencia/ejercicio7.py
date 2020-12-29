# Ejercicio 7

# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro.
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta.
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés.
# Tendrá un método para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar la información,
# datos del titular plazo, interés y total de interés.
# Crear al menos un objeto de cada subclase.

class Cuenta():
    
    def __init__(self,titular,cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def __str__(self):
        return "Titular: {}, Cantidad: {}".format(self.titular,self.cantidad)

class PlazoFijo(Cuenta):
    
    def __init__(self,titular, cantidad, plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo = plazo
        self.interes = interes

    def importeInteres(self):
        return (self.cantidad*self.interes)/100

    def __str__(self):
        return super().__str__() + ", Plazo: {}, Interés: {}, Total de interés: {}".format(self.plazo,self.interes,self.importeInteres())

class CajaAhorro(Cuenta):
    
    def __init__(self,titular,cantidad):
        super().__init__(titular,cantidad)

    def __str__(self):
        return super().__str__()


#Objetos
caja1=CajaAhorro("Manuel",5000)
print(caja1)
 
plazo1=PlazoFijo("Isabel",8000,365,1.2)
print(plazo1)