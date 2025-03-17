from nodo import NodoDoble

class ListaDobleOrdenada:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertar_ordenado(self, persona):
        nuevo_nodo = NodoDoble(persona)
        if not self.head:
            self.head = self.tail = nuevo_nodo
        elif persona.edad < self.head.data.edad:
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.next and actual.next.data.edad < persona.edad:
                actual = actual.next
            nuevo_nodo.next = actual.next
            if actual.next:
                actual.next.prev = nuevo_nodo
            else:
                self.tail = nuevo_nodo
            actual.next = nuevo_nodo
            nuevo_nodo.prev = actual

    def imprimir(self):
        actual = self.head
        contador = 0
        while actual:
            print(f"{contador + 1}. {actual.data}")
            actual = actual.next
            contador += 1
        print(f"Total de personas: {contador}")

    def buscar_por_edad(self, edad):
        if not self.head:
            print("La lista está vacía.")
            return
        
        # Calcular distancia desde head y tail
        distancia_head = abs(self.head.data.edad - edad)
        distancia_tail = abs(self.tail.data.edad - edad)
        
        # Elegir dirección de búsqueda
        if distancia_head <= distancia_tail:
            actual = self.head
            step = lambda x: x.next
        else:
            actual = self.tail
            step = lambda x: x.prev
        
        encontrados = []
        while actual:
            if actual.data.edad == edad:
                encontrados.append(actual.data)
            actual = step(actual)
        
        if not encontrados:
            print("Nadie tiene esa edad.")
        else:
            for persona in encontrados:
                print(persona)

    def buscar_por_nombre(self, texto):
        actual = self.head
        encontrados = []
        while actual:
            if texto.lower() in actual.data.nombre.lower():
                encontrados.append(actual.data)
            actual = actual.next
        
        if not encontrados:
            print("No se encontraron personas con ese nombre.")
        else:
            for persona in encontrados:
                print(persona)

    def buscar_por_apellido(self, texto):
        actual = self.head
        encontrados = []
        while actual:
            if (texto.lower() in actual.data.apellido1.lower() or
                texto.lower() in actual.data.apellido2.lower()):
                encontrados.append(actual.data)
            actual = actual.next
        
        if not encontrados:
            print("No se encontraron personas con ese apellido.")
        else:
            for persona in encontrados:
                print(persona)

    def borrar_por_posicion(self, posicion):
        if posicion < 1:
            print("Posición inválida: debe ser un número mayor o igual a 1.")
            return
        
        # Calcular longitud de la lista
        longitud = 0
        actual = self.head
        while actual:
            longitud += 1
            actual = actual.next
        
        if posicion > longitud:
            print(f"Posición inválida: la lista solo tiene {longitud} elementos.")
            return
        
        posicion -= 1  # Convertir a índice 0-based

        if posicion == 0:  # Borrar el primer nodo
            if self.head:
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None  # La lista quedó vacía
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
                if actual.next:  # Si hay un nodo después del borrado
                    actual.next.prev = actual
                else:
                    self.tail = actual  # Actualizar tail si se borró el último nodo
            else:
                print(f"Posición inválida: la lista solo tiene {posicion} elementos.")