class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super()
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(
            self.velocidad, self.cilindrada)


# Completa el ejercicio aquí

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} carga".format(self.carga)



class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {} tipo".format(self.tipo)
        
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
       super().__init__(color,ruedas,tipo)
       self.velocidad=velocidad
       self.cilindrada=cilindrada

    def __str__(self):
        return super().__str__()+", {} km/h, {} cc".format(self.velocidad,self.cilindrada)


miCoche = Coche("negro",4,200,900)
miCamioneta = Camioneta("Azul",4,120,560,200)
miBici = Bicicleta("Roja",2,"Urbano")
miMoto = Motocicleta("Amarilla",2,"Susuki",200,265)

vehiculos = [miCoche,miCamioneta,miBici,miMoto]

def catalogar(listaVehiculos, ruedas=None):
    contador = 0
    lista = []
    for i in listaVehiculos:
        print(type(i).__name__, i)

        if i.ruedas == ruedas:
            contador = contador+1
            lista.append(i)

    print(f"\nSe han encontrado {contador} vehículos con {ruedas} ruedas:")
    for i in lista:
        print(type(i).__name__, i)

while True:
    try:
        ruedas = int(input("Ingrese el número de ruedas a categorizar: 2,4\n"))
        if ruedas in [2,4]:
            catalogar(vehiculos,ruedas)
            break
        else:
            raise TypeError("Por favor, ingrese los valores permitidos")
    except ValueError as error:
        print(error)
    except TypeError as error:
        print(error)