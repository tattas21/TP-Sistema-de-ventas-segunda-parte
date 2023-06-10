from Vehiculos import *
from Biblioteca import *

class Nodo:
    def __init__(self, vehiculo, siguiente = None):
        self.vehiculo = vehiculo
        self.siguiente = siguiente

        

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, vehiculo):
        nuevo_nodo = Nodo(vehiculo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            return
    
    def eliminar(self, id):
        
        if self.cabeza is None:
            return
        elif self.cabeza.vehiculo.id == id:
            self.cabeza = self.cabeza.siguiente   
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.siguiente.vehiculo.id == id:
                    if actual.siguiente.siguiente == None:
                        actual.siguiente = None
                        return self
                    else:
                        actual.siguiente = actual.siguiente.siguiente
                    return self
                actual = actual.siguiente
    
    def __str__(self):
        if self.cabeza is None:
            return "La lista está vacía"
        else:
            actual = self.cabeza
            resultado = str(actual.vehiculo)
            while actual.siguiente is not None:
                actual = actual.siguiente
                resultado += f"\n{str(actual.vehiculo)}"
            return resultado
    def list(self):
        lista = []
        nodo = self.cabeza
        while nodo is not None:
            lista.append(nodo.vehiculo)
            nodo = nodo.siguiente
        return lista
    def ultimo_nodo(self):
        while self.cabeza.siguiente is not None:
            self.cabeza = self.cabeza.siguiente
        return self.cabeza
    def vaciar(self):
        self.cabeza = None

class Stock(ListaEnlazada):
    def __init__(self):
        self = ListaEnlazada()

    def modificar(self, id, dato, nuevo_dato):
        if self.cabeza is None:
            return
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.vehiculo.id == id:
                    match dato:
                        case "marca":
                            actual.vehiculo.marca = nuevo_dato
                            return
                        case "modelo":
                            actual.vehiculo.modelo = nuevo_dato
                            return
                        case "precio":
                            actual.vehiculo.precio = nuevo_dato
                            return
                        case "autonomia":
                            actual.vehiculo.autonomia = nuevo_dato
                            return
                        case "uso":
                            actual.vehiculo.uso = nuevo_dato
                            return
                        case "carga maxima":
                            actual.vehiculo.carga_maxima = nuevo_dato
                            return
                        case "velocidad maxima":
                            actual.vehiculo.velocidad_maxima = nuevo_dato
                            return
                        case "tiempo carga":
                            actual.vehiculo.tiempo_carga = nuevo_dato
                            return
                        case "asientos":
                            actual.vehiculo.asientos = nuevo_dato
                            return
                        case "tamaño baul":
                            actual.vehiculo.tamaño_baul = nuevo_dato
                            return
                        case _:
                            return print("Dato ingresado no válido")
                            
                actual = actual.siguiente
            return print("No se encontró el vehículo")
    def buscar(self, marca, modelo, precio, autonomia, uso):
        listav = []
        if self.cabeza is None:
            return
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.vehiculo.marca == marca or actual.vehiculo.modelo == modelo or actual.vehiculo.precio == precio or actual.vehiculo.autonomia == autonomia or actual.vehiculo.uso == uso:
                    listav.append(actual.vehiculo)
                actual = actual.siguiente
            return listav

    def descargar_stock(self,nombre_archivo, variable):
        self.vaciar()
        try:
            with open(nombre_archivo, "r") as archivo:
                lineas = archivo.readlines()
                vehiculo=None
                for linea in lineas:
                    campos = linea.strip().split(",")
                    if campos[0] == "utilitario":
                        if variable == True:
                            vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)

                    elif campos[0] == "deportivo":
                        if variable == True:
                            vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "electrico":
                        if variable == True:
                            vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "van":
                        if variable == True:
                            vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "compacto":
                        if variable == True:
                            vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)

                    self.agregar(vehiculo)
            archivo.close()

        except FileNotFoundError:
            print("El archivo no existe")
        return self
    
    def guardar_stock(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            if self.cabeza is not None:
                actual = self.cabeza
                tipo= None
                datos=None
                while actual is not None:
                    if isinstance(actual.vehiculo, Utilitario):
                        tipo = "utilitario"
                        datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.carga_maxima},{actual.vehiculo.id}\n"
                    elif isinstance(actual.vehiculo, Deportivo):
                        tipo = "deportivo"
                        datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.velocidad_maxima},{actual.vehiculo.id}\n"
                    elif isinstance(actual.vehiculo, Electrico):
                        tipo = "electrico"
                        datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tiempo_carga},{actual.vehiculo.id}\n"
                    elif isinstance(actual.vehiculo, Van):
                        tipo = "van"
                        datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso}, {actual.vehiculo.asientos},{actual.vehiculo.id}\n"
                    elif isinstance(actual.vehiculo, Compacto):
                        tipo = "compacto"
                        datos = f"{actual.vehiculo.marca},{actual.vehiculo.modelo},{actual.vehiculo.precio},{actual.vehiculo.autonomia},{actual.vehiculo.uso},{actual.vehiculo.tamaño_baul},{actual.vehiculo.id}\n"
                    archivo.write(f"{tipo},{datos}")
                    actual = actual.siguiente

    def eliminar_vehiculo(self):
        id = input("Ingrese el id del vehiculo a eliminar: ")
        actual = self.cabeza 
        while actual is not None:
            if actual.vehiculo.id == id:
                self.eliminar(id)
                print(f"El vehiculo {actual.vehiculo.marca} {actual.vehiculo.modelo} con ID: {actual.vehiculo.id} fue eliminado.")
                self.guardar_stock("stock.txt")
                return
            actual = actual.siguiente
    def modificar_dato_vehiculo(self):
        n = True
        while n == True:
            id = input("Ingrese el id del vehiculo a modificar: ")
            dato = input("Ingrese el dato a modificar: ")
            dato = dato.lower()
            nuevo_dato = input("Ingrese el nuevo dato: ")
            self.modificar(id, dato, nuevo_dato)
            print("Desea modificar otro dato? (s/n)")
            if input() == "s":
                n = True
            else:
                n = False
        self.guardar_stock("stock.txt")
    def agregar_vehiculo(self, registro):
        i = numero_id(self.descargar_stock("stock.txt", registro))
        n = True 
        while n == True:
            agregar_vehiculo_tipo(n, self.descargar_stock("stock.txt", registro), str(i))
            if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
                i = int(i) + 1
                n = True
            else:
                n = False
        self.guardar_stock("stock.txt")