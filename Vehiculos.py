
class Vehiculo:
# La clase principal "Vehiculo" representa un vehículo genérico y tiene los atributos comunes a todos los vehículos, 
# como el modelo, marca, precio, autonomía, uso y un ID.
    def __init__(self, modelo, marca, precio,  autonomia, uso, id):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.autonomia = autonomia
        self.uso = uso
        self.id = id
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio},Autonomia: {self.autonomia}, Uso: {self.uso}"

class Utilitario(Vehiculo):
# La clase "Utilitario" representa un vehículo utilitario y agrega un atributo adicional llamado "carga_maxima"
    def __init__(self, marca, modelo, precio, autonomia, uso, carga_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.carga_maxima = carga_maxima
        self.tipo = "utilitario"
    def __str__(self):
        return f'Tipo: {self.tipo}, ' + super().__str__() + f", Carga máxima: {self.carga_maxima}, ID: {self.id}"
        
class Deportivo(Vehiculo):
# La clase "Deportivo" representa un vehículo deportivo y agrega un atributo adicional llamado "velocidad_maxima"
    def __init__(self, marca, modelo, precio, autonomia, uso, velocidad_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.velocidad_maxima = velocidad_maxima
        self.tipo = "deportivo"
    def __str__(self):
        return f'Tipo: {self.tipo}, ' + super().__str__() + f", Velocidad máxima: {self.velocidad_maxima}, ID: {self.id}"
        
class Electrico(Vehiculo):
# La clase "Electrico" representa un vehículo eléctrico y agrega un atributo adicional llamado "tiempo_carga"
    def __init__(self, marca, modelo, precio,autonomia, uso, tiempo_carga, id):
        super().__init__(modelo, marca, precio,autonomia, uso,  id)
        self.tiempo_carga = tiempo_carga
        self.tipo = "electrico"
    def __str__(self):
        return f'Tipo: {self.tipo}, ' + super().__str__() + f", Tiempo de carga: {self.tiempo_carga}, ID: {self.id}"
        
class Van(Vehiculo):
# La clase "Van" representa un vehículo van y agrega un atributo adicional llamado "asientos"
    def __init__(self, marca, modelo, precio,autonomia, uso, asientos, id):
        super().__init__(modelo, marca, precio, autonomia, uso, id)
        self.asientos = asientos
        self.tipo = "van"

    def __str__(self):
        return f'Tipo: {self.tipo}, ' + super().__str__() + f", Asientos: {self.asientos}, ID: {self.id}"
        
class Compacto(Vehiculo):
# La clase "Compacto" representa un vehículo compacto y agrega un atributo adicional llamado "tamaño_baul"
    def __init__(self, marca, modelo, precio, autonomia, uso,tamaño_baul, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.tamaño_baul = tamaño_baul
        self.tipo = "compacto"
    def __str__(self):
        return f'Tipo: {self.tipo}, ' + super().__str__() + f", Tamaño del baul: {self.tamaño_baul}, ID: {self.id}"