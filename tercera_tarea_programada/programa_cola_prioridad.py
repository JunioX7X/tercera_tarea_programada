from cola_prioridad import ColaPrioridad
from persona import Persona

cola = ColaPrioridad()

while True:
    print("\n1. Agregar persona\n2. Desencolar\n3. Imprimir cola\n4. Salir")
    opcion = input("Opción:------- ")
    if opcion == "1":
        nombre = input("Nombre: ")
        apellido1 = input("Primer apellido: ")
        apellido2 = input("Segundo apellido: ")
        edad = int(input("Edad: "))
        persona = Persona(nombre, apellido1, apellido2, edad)
        cola.encolar(persona)
    elif opcion == "2":
        eliminado = cola.desencolar()
        if eliminado:
            print(f"Persona desencolada--------: {eliminado}")
        else:
            print("Cola vacía")
    elif opcion == "3":
        cola.imprimir()
    elif opcion == "4":
        print("------------Adiós-----------")
        break