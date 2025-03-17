from lista_enlazada_ordenada import ListaEnlazadaOrdenada
from persona import Persona

lista = ListaEnlazadaOrdenada()

while True:
    print("\n1. Agregar persona\n2. Listar\n3. Buscar\n4. Borrar\n5. Salir")
    opcion = input("Opción:---------------- ")
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        lista.insertar_ordenado(persona)
    elif opcion == "2":
        lista.imprimir()
    elif opcion == "3":
        print("\n1. Buscar por edad\n2. Buscar por nombre\n3. Buscar por apellido")
        sub_opcion = input("Sub-opción: ")
        if sub_opcion == "1":
            edad = int(input("Edad a buscar: "))
            lista.buscar_por_edad(edad)
        elif sub_opcion == "2":
            texto = input("Texto a buscar en nombre: ")
            lista.buscar_por_nombre(texto)
        elif sub_opcion == "3":
            texto = input("Texto a buscar en apellido: ")
            lista.buscar_por_apellido(texto)
    elif opcion == "4":
        posicion = int(input("Posición a borrar:------ "))
        lista.borrar_por_posicion(posicion)
    elif opcion == "5":
        print("------------Adiós---------------")
        break