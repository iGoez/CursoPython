import pickle

class Persona:

    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Se ha creado una persona con el nombre de ",self.nombre)

    def __str__(self):
        return "{}, {}, {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    personas = []

    def __init__(self):
        # el ab+ me permite abrir el texto del archivo binario y agregar texto al final sin modificarlo
        try:
            listaDePersonas = open("serializacion/ficheroNombres","ab+")
            # Después de agregar información tenemos que ubicar el cursor al principio porque al leer éste estará al final
            listaDePersonas.seek(0)
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas del archivo".format(len(self.personas)))
        except:
            print("El archivo se encuentra vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)


    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasFichero()

    def guardarPersonasFichero(self):
        try:
            listaDePersonas = open("serializacion/ficheroNombres","wb")
            pickle.dump(self.personas,listaDePersonas)
        finally:
            listaDePersonas.close()
            del(listaDePersonas)
        
    def mostrarInformacionFichero(self):
        for i in self.personas:
            print(i)

miLista=ListaPersonas()
p = Persona("Sandra", "Femenina", 25)
miLista.agregarPersonas(p)
miLista.mostrarInformacionFichero()
