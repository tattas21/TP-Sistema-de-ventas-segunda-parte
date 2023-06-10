class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)
# Este método agrega un elemento al final de la cola. 
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("La cola está vacía.")
# Este método elimina y devuelve el primer elemento de la cola. Verifica si la cola no está vacía llamando al método esta_vacia(). 
# Si la cola no está vacía, utiliza el método pop(0) para eliminar y devolver el primer elemento de la lista items. 
# Si la cola está vacía, lanza una excepción IndexError con un mensaje indicando que la cola está vacía.
    def esta_vacia(self):
        return len(self.items) == 0
# Este método verifica si la cola está vacía. Comprueba si la longitud de la lista items es igual a cero
    def vaciar(self):
        self.items = []
# Este método vacía la cola. Asigna una lista vacía a la lista items.