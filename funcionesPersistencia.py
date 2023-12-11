##################### Funciones de Persistencia #######################

def obtenerDatos():
    contactos = {}
    try:
        with open("contactos.txt", "r") as archivo:
            for linea in archivo:
                contacto, numero = linea.strip().split(":")
                contactos[contacto] = numero
    except FileNotFoundError:
        print("Error! El archivo 'contactos.txt' no existe aún. Se creará al guardar las modificaciones en la Agenda.")
    return contactos

# Función para obtener los datos. Es útil para saber si hay un Documento anterior que albergue ciertos datos ingresados por el usuario

def modificarDatos(contactos):
    with open("contactos.txt", "w") as archivo:
        for contacto, numero in contactos.items():
            archivo.write(f"{contacto}: {numero}\n")

# Función para modificar los datos. Se utiliza en todas aquellas Funciones que cambien el archivo .txt.