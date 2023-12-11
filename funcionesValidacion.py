####################### Funciones de Validación ######################

def validarContacto():
    while True:
        contacto = input("\nIngrese el nombre del contacto: ").strip().title()
        if contacto:
            return contacto
        else: 
            print("\nPor favor, ingrese un nombre de contacto valido.")
# Función para validar el nombre del contacto ingresado 

def validarNumeroTelefono():
    while True:
        numeroTelefono = input ("\nIngrese el numero de telefono: ").strip()
        if numeroTelefono:
            try:
                numeroTelefono = int(numeroTelefono)
                return numeroTelefono
            except ValueError:
                print("\nError! El numero de telefono debe contener únicamente numeros enteros.")
        else:
            print("\nPor favor, ingrese un numero de telefono valido.")
        
# Función para validar el numero de telefono ingresado