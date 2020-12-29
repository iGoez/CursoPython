import pickle

class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ",self.marca, "\nModelo: ",self.modelo,
        "\nEn marcha: ",self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena)

cocheUno = Vehiculo("Uno","Uno")
cocheDos = Vehiculo("Dos","Dos")
cocheTres = Vehiculo("Tres","Tres")

coches = [cocheUno,cocheDos,cocheTres]

fichero_coches = open("serializacion/listaCoches", "wb")

pickle.dump(coches,fichero_coches)

fichero_coches.close()
del(fichero_coches)

fichero_coches = open("serializacion/listaCoches", "rb")
lista= pickle.load(fichero_coches)

for i in lista:
    print(i.estado())

fichero_coches.close()
del(fichero_coches)