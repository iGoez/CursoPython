# Ejercicio 5
# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
# Además deberá mostrar un menú con las siguientes opciones

# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

class Agenda():

    def __init__(self):
        self.contactos = []


    def addContacto(self,nombre,telefono,email):
        self.contactos.append({"Nombre":nombre,"Telefono":telefono,"Email":email})

    def listarContactos(self):
        contacts = ""
        if len(self.contactos) == 0:
            contacts = "No hay contactos para listar"
        else:
            for i in self.contactos:
                contacts = "{} Nombre: {}, Teléfono: {}, Email: {}\n".format(contacts,i["Nombre"],i["Telefono"],i["Email"])
        return contacts
    
    def buscarContacto(self,nombre):
        contacto = ""
        for i in self.contactos:
            if nombre.lower() == i["Nombre"].lower():
                contacto = "{} Nombre: {}, Teléfono: {}, Email: {}\n".format(contacto,i["Nombre"],i["Telefono"],i["Email"])
                break
        return contacto
    
    def contactoExiste(self, nombre):
        index = -1
        for i in self.contactos:
            index = index+1
            if nombre.lower() == i["Nombre"].lower():
                return index
        return -1

    def editarContacto(self,index,nombre,telefono,email):
        if nombre != str(1):
            self.contactos[index]["Nombre"] = nombre
        if telefono != str(1):
            self.contactos[index]["Telefono"] = telefono
        if email != str(1):
            self.contactos[index]["Email"] = email
        
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
                    index = miAgenda.contactoExiste(nombre)
                    if index != -1:
                        print("Presione 1 si no quiere modificar el campo")
                        nombre = input("Ingrese un nuevo nombre: ")
                        print("Presione 1 si no quiere modificar el campo")
                        telefono = int(input("Ingrese un nuevo telefono: "))
                        print("Presione 1 si no quiere modificar el campo")
                        email = input("Ingrese un nuevo email: ")
                        miAgenda.editarContacto(index,nombre,telefono,email)
                    else:
                        raise TypeError("El contacto no existe")
                else:
                    raise TypeError("El número no es válido")
        except ValueError as error:
            print("Por favor, ingrese un número")
        except TypeError as error:
            print(error)
menu()