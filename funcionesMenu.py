######################### Funciones del Menu ##########################

from funcionesValidacion import validarContacto, validarNumeroTelefono
from funcionesPersistencia import modificarDatos

def agregarContacto(contactos):
    contacto = validarContacto()
    if contacto not in contactos:
        numero = validarNumeroTelefono()
        contactos[contacto] = numero
        modificarDatos(contactos)
        print(f"\n{contacto} fue agregado/a correctamente a la Agenda de Contactos.")
    else:
        print(f"\n{contacto} ya se encuentra en la Agenda de Contactos")

# Función para agregar un contacto a la agenda

def eliminarContacto(contactos):
    
    if contactos:
        contacto = input("\nIngrese el nombre del contacto que desea eliminar: ").title()
        if contacto in contactos:
            contactos.pop(contacto)
            modificarDatos(contactos)
            print("\nContacto eliminado correctamente.")
        else:
            print(f"\n{contacto} no se encuentra agendado.")
    else:
        print("\nError! No se encuentran contactos en la Agenda.")

# Función para eliminar algun contacto de la agenda

def modificarContacto(contactos):
    
    if contactos:
        contacto = input("\nIngrese el nombre del contacto que desea modificar: ").title()
        if contacto in contactos:
            print("\nA continuacion, ingrese el nuevo numero de telefono del contacto indicado.")
            nuevoNumero = validarNumeroTelefono()
            contactos[contacto] = nuevoNumero
            modificarDatos(contactos)
            print(f"\nEl numero de telefono de {contacto} ha sido modificado correctamente.")
        else:
            print(f"\n{contacto} no se encuentra agendado/a.")
    else:
        print("\nError! No se encuentran contactos en la Agenda.")

# Función para modificar el numero de telefono de algun contacto presente en la agenda

def buscarContacto(contactos):
    
    if contactos:
        contacto = input("\nIngrese el contacto que desea buscar: ").title()
        if contacto in contactos:
            print(f"\n° {contacto}: {contactos[contacto]}")
        else:
            print(f"\n{contacto} no se encuentra agendado/a.")
    else:
        print("\nError! No se encuentran contactos en la Agenda.")

# Función para buscar un contacto dentro de la agenda

def mostrarContactos(contactos):
    if contactos:
        print("""\n******** CONTACTOS ********""")
        print("\nContacto ---> Numero")
        for contacto, numero in contactos.items():
            print(f"\n ° {contacto}: {numero}")
    else:
        print("\nNo se encuentra agendado ningún contacto")
        
# Función para mostrar los contactos que se encuentran dentro de la agenda.