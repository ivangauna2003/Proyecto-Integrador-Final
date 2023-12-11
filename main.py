"""
Consigna

Deberás crear una aplicación de consola la cual simulará una “agenda
telefónica”, la misma permitirá:
- Gestionar contactos
- Agregar
- Borrar
- Modificar
- Mostrar contactos.
- Salir del programa
"""
import os # Se importa 'os' para utilizar la función 'os.system' con el fin de limpiar la consola

from funcionesMenu import * # Se importan las Funciones presentes en el archivo 'funcionesMenu.py' de manera generica con el '*'
from funcionesPersistencia import obtenerDatos # Se importa en especifico la funcion para obtener los datos desde el archivo 'funcionesPersistencia.py'


###############################################################################################
#                                   Código Principal                                          #
###############################################################################################

contactos = obtenerDatos()

while True:
    os.system("cls")
    print("""
        **********************
        **AGENDA TELEFONICA***
        **********************
        [1] Agregar contacto
        [2] Eliminar contacto
        [3] Modificar contacto
        [4] Buscar contacto
        [5] Mostrar contactos
        [6] Salir
        """)
    opcion = input("Seleccione su opción: ")
    if opcion == "1":
        agregarContacto(contactos)
        input("\nPresione Enter para continuar.")
        os.system("cls")

    elif opcion == "2":
        eliminarContacto(contactos)
        input("\nPresione Enter para continuar.")
        os.system("cls")

    elif opcion == "3":
        modificarContacto(contactos)
        input("\nPresione Enter para continuar.")
        os.system("cls")

    elif opcion == "4":
        buscarContacto(contactos)
        input("\nPresione Enter para continuar.")
        os.system("cls")

    elif opcion == "5":
        mostrarContactos(contactos)
        input("\nPresione Enter para continuar.")
        os.system("cls")

    elif opcion == "6":
        print("\nHasta luego")
        input("\nPresione Enter para finalizar. . .")
        os.system("cls")
        break

    else:
        print("\nSeleccione una opcion correcta")
        input("")
        os.system("cls")