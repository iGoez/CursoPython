#El método cambiará su comportamiento dependiendo de los argumentos que se le pasen

#Ejercicio sin polimorfismo
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

#Ejercicios con polimorfismo

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)