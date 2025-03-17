class NodoSimple:
    def __init__(self, data):
        self.data = data  # Objeto Persona
        self.next = None

class NodoDoble(NodoSimple):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None