from nodo import NodoSimple

class ColaPrioridad:
    def __init__(self):
        self.head = None

    def encolar(self, persona):
        nuevo_nodo = NodoSimple(persona)
        if persona.edad > 65:
            if not self.head or self.head.data.edad <= 65:
                nuevo_nodo.next = self.head
                self.head = nuevo_nodo
            else:
                actual = self.head
                # Buscar el último nodo con edad >65
                while actual.next and actual.next.data.edad > 65:
                    actual = actual.next
                nuevo_nodo.next = actual.next
                actual.next = nuevo_nodo
        else:
            if not self.head:
                self.head = nuevo_nodo
            else:
                actual = self.head
                while actual.next:
                    actual = actual.next
                actual.next = nuevo_nodo

    def desencolar(self):
        if self.head:
            eliminado = self.head
            self.head = self.head.next
            return eliminado.data
        return None

    def imprimir(self):
        actual = self.head
        while actual:
            print(actual.data)
            actual = actual.next