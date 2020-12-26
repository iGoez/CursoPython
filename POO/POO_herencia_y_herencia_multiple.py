# Herencia sirve para reutilizar código en caso de crear objetos similares.
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
    
#Forma de heredar de una clase
class Moto(Vehiculo):
    caballito =""

    def hacer_caballido(self):
        self.caballito="Haciendo el caballito"

    #Para sobreescribir un método de la clase padre hay que colocar el mismo nombre del método
    #y los mismo parametros que tiene el método. Se pueden agregar más parametros.
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,
              "\nCaballito: ",self.caballito)

class Furgoneta(Vehiculo):
    def carga(self,cargar):
        self.cargado = cargar
        if self.cargado:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class VehiculoElectrico():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargado=True

#Herencia múltiple
#Cuando hay herencia múltiple y hay varios constructores, entonces se tomará el constructor de la clase del primer argumento 
class BicicletaElectrica(Vehiculo,VehiculoElectrico):
    pass

#Como también hereda el constructor entonces hay que pasarle parametros
miMoto = Moto("Honda","CBR")
miMoto.hacer_caballido()
miMoto.estado()

miFurgoneta = Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Herencia múltiple
#Cuando hay herencia múltiple y hay varios constructores, entonces se tomará el constructor de la clase del primer argumento 
miBici = BicicletaElectrica("Orbea","HC130")
