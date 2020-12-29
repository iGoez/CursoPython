# Ejercicio 5
# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
# Además deberá mostrar un menú con las siguientes opciones

# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

class Contacto():
    
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono=telefono
        self.email=email

    def informacion(self):
        return "Nombre: {}, Teléfono: {}, Email: {}".format(self.nombre,self.telefono,self.email)

class Agenda():

    def __init__(self):
        self.contactos = []


    def addContacto(self,nombre,telefono,email):
        nuevoContacto = Contacto(nombre,telefono,email)
        self.contactos.append(nuevoContacto)

    def listarContactos(self):
        contacts = ""
        if len(self.contactos) == 0:
            contacts = "No hay contactos para listar"
        else:
            for i in range(len(self.contactos)):
                contacts = f"{contacts} {self.contactos[i].informacion()}\n"
        return contacts
    
    def buscarContacto(self,nombre):
        contacto = ""
        for i in self.contactos:
            if nombre.lower() == i.nombre.lower():
                contacto = i.informacion()
                break
        return contacto
    
    def contactoExiste(self, nombre):
        for i in range(len(self.contactos)):
            if nombre.lower() == self.contactos[i].nombre.lower():
                return i
        return -1

    def editarContacto(self,id,nombre,telefono,email):
        if nombre != str(1):
            self.contactos[id].nombre = nombre
        if telefono != str(1):
            self.contactos[id].telefono = telefono
        if email != str(1):
            self.contactos[id].email = email
        
def menu():
    miAgenda = Agenda()
    print("1: Añadir contacto\n2: Lista de contactos \n3: Buscar contacto \n4: Editar contacto \n5: Cerrar agenda")
    while True:
        try:
            numero = int(input("Ingrese el número de la acción a realizar.\n"))
            if numero in [1,2,3,4,5]:
                if numero == 5:
                    break
                elif numero == 1:
                    nombre = input("Ingrese el nombre del nuevo contacto: ")
                    telefono = int(input("Ingrese el teléfono del nuevo contacto: "))
                    email = input("Ingrese el email del nuevo contacto: ")
                    miAgenda.addContacto(nombre,telefono,email)
                elif numero == 2:
                    print(miAgenda.listarContactos())
                elif numero == 3:
                    nombre = input("Ingrese el nombre del contacto: ")
                    print(miAgenda.buscarContacto(nombre))
                elif numero == 4:
                    nombre = input("Ingrese el nombre del contacto a editar: ")
                    id = miAgenda.contactoExiste(nombre)
                    if id != -1:
                        print("Presione 1 si no quiere modificar el campo")
                        nombre = input("Ingrese un nuevo nombre: ")
                        print("Presione 1 si no quiere modificar el campo")
                        telefono = int(input("Ingrese un nuevo telefono: "))
                        print("Presione 1 si no quiere modificar el campo")
                        email = input("Ingrese un nuevo email: ")
                        miAgenda.editarContacto(id,nombre,telefono,email)
                    else:
                        raise TypeError("El contacto no existe")
                else:
                    raise TypeError("El número no es válido")
        except ValueError as error:
            print("Por favor, ingrese un número")
        except TypeError as error:
            print(error)
menu()