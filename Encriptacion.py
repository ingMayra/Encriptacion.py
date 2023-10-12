import archivos

opcion = 0
archivo = "archivo.txt"

archivos.genpiperar_clave ()
clave= archivos.cargar_clave()

while opcion != 5:
    print("\nSelecciona una Opcion")
    print("1.Leer Archivo\n2.Agregar texto al archivo\n3.Encriptar\n4.Desencriptar\n5. Salir")
    opcion = int (input("Ingresa una opcion: "))

    if opcion == 1:
        print("El contenido del archivo es: ")
        archivos.LeerArchivo(archivo)
    elif opcion == 2:
        linea = input("Introduce el texto que deseas agregar al archivo: ")
        archivos.escribirArchivo(linea, archivo)
    elif opcion == 3:
        archivos.encriptar(archivo, clave)
        print("archivo encriptado correctamente")

    elif opcion == 4:
        archivos.desencriptar(archivo,clave)
        print("archivo desincriptado correctamente")
    else:
       print("¡La opcion seleccionada en Incorrecta!")
