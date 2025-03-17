from nodo import NodoSimple

class ListaEnlazadaOrdenada:
    def __init__(self):
        self.head = None

    def insertar_ordenado(self, persona):
        nuevo_nodo = NodoSimple(persona)
        if not self.head or persona.edad < self.head.data.edad:
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next and actual.next.data.edad < persona.edad:
                actual = actual.next
            nuevo_nodo.next = actual.next
            actual.next = nuevo_nodo

    def imprimir(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next

    def buscar_por_edad(self, edad):
        actual = self.head
        while actual:
            if actual.data.edad == edad:
                print(actual.data)
            actual = actual.next

    def buscar_por_nombre(self, texto):
        actual = self.head
        while actual:
            if texto.lower() in actual.data.nombre.lower():
                print(actual.data)
            actual = actual.next

    def buscar_por_apellido(self, texto):
        actual = self.head
        while actual:
            if (texto.lower() in actual.data.apellido1.lower() or
                texto.lower() in actual.data.apellido2.lower()):
                print(actual.data)
            actual = actual.next

    def borrar_por_posicion(self, posicion):
            # Calcular longitud
        longitud = 0
        actual = self.head
        while actual:
            longitud += 1
            actual = actual.next
        if posicion > longitud:
            print("Posición inválida: debe ser un número mayor o igual a 1.")
            return

        posicion -= 1  # Convertir la posición del usuario (1-based) a índice interno (0-based)

        if posicion == 0:  # Borrar el primer nodo
            if self.head:
                self.head = self.head.next
            else:
                print("La lista está vacía.")
        else:
            actual = self.head
            for _ in range(posicion - 1):  # Avanzar hasta el nodo anterior al que se borrará
                if actual.next:
                    actual = actual.next
                else:
                    print(f"Posición inválida: la lista solo tiene {posicion} elementos.")
                    return
            if actual.next:  # Si existe el nodo a borrar
                actual.next = actual.next.next
            else:
                print(f"Posición inválida: la lista solo tiene {posicion} elementos.")