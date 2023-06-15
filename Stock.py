from Vehiculos import *
from Biblioteca import *

class Nodo:
# La clase Nodo representa un nodo de una lista enlazada. Cada nodo contiene un objeto "dato"
# (en este caso se llama vehiculo pero no solo son objetos vehiculos) y una referencia al siguiente nodo en la lista.


    def __init__(self, vehiculo, siguiente = None):
        self.vehiculo = vehiculo
        self.siguiente = siguiente

        

class ListaEnlazada:
# La clase ListaEnlazada implementa una lista enlazada utilizando la clase Nodo. 
# Tiene un atributo cabeza que apunta al primer nodo de la lista.
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, vehiculo):
# Agrega un nuevo nodo al final de la lista.
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
# Elimina el nodo que contiene el objeto "dato" ingresado.
        
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
# Devuelve una lista con los objetos "dato" de cada nodo.
        lista = []
        nodo = self.cabeza
        while nodo is not None:
            lista.append(nodo.vehiculo)
            nodo = nodo.siguiente
        return lista
    def ultimo_nodo(self):
# Devuelve el último nodo de la lista.
        while self.cabeza.siguiente is not None:
            self.cabeza = self.cabeza.siguiente
        return self.cabeza
    def vaciar(self):
# Vacía la lista.
        self.cabeza = None
def lista_a_lista_enlazada(lista):
    lista_enlazada = ListaEnlazada()
    for elemento in lista:
        lista_enlazada.agregar(elemento)
    return lista_enlazada

class Stock(ListaEnlazada):
# La clase Stock hereda de ListaEnlazada y agrega métodos adicionales para gestionar el stock de vehículos. 
    def __init__(self):
        self = ListaEnlazada()

    def modificar(self, id, dato, nuevo_dato):
# Modifica un dato específico del vehículo con el id especificado.
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
# Busca y devuelve una lista de vehículos que coinciden con los criterios especificados.
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
# Descarga el stock de vehículos desde un archivo y lo guarda en la lista enlazada.
        self.vaciar()
        try:
            with open(nombre_archivo, "r") as archivo:
                lineas = archivo.readlines()
                vehiculo=None
                for linea in lineas:
                    campos = linea.strip().split(",")
                    if campos[0] == "utilitario":
                            vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                    elif campos[0] == "deportivo":
                            vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                    elif campos[0] == "electrico":
                            vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                    elif campos[0] == "van":
                            vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                    elif campos[0] == "compacto":
                            vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        

                    self.agregar(vehiculo)
            archivo.close()

        except FileNotFoundError:
            print("El archivo no existe")
        return self
    
    def guardar_stock(self, nombre_archivo):
# Guarda el stock de vehículos de la lista enlazada en un archivo.
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
        archivo.close()
        print(f"Stock guardado en el archivo {nombre_archivo}")


    def eliminar_vehiculo(self):
# Permite al usuario eliminar un vehículo del stock a partir del ID.
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
# Permite al usuario modificar un dato específico de un vehículo en el stock.
        n = True
        while n == True:
            id = input("Ingrese el id del vehiculo a modificar: ")
            dato = input("Ingrese el dato a modificar: ")
            dato = dato.lower()
            nuevo_dato = input("Ingrese el nuevo dato: ")
            self.modificar(id, dato, nuevo_dato)
            salir = input("Desea modificar otro dato? (s/n): ")
            salir = input.lower()
            if salir == "s":
                n = True
            else:
                n = False
        self.guardar_stock("stock.txt")
    def agregar_vehiculo(self, registro):
# Permite al usuario descargrar el stock, agregar vehículos y guardar el stock despues.
        self.descargar_stock("stock.txt", registro)
        i = self.numero_id()
        self.vaciar()
        self.descargar_stock("stock.txt", registro)
        n = True 
        while n == True:
            self.agregar_vehiculo_tipo(str(i))
            if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
                i = int(i) + 1
                n = True
            else:
                n = False
        self.guardar_stock("stock.txt")
    
    def agregar_vehiculo_tipo(self,i):
# Permite al usuario agregar un vehículo de un tipo específico al stock.
        n = True
        l = True
        while l:
            tipo= input("Ingrese el tipo de vehículo que desea agregar: ")
            tipo=tipo.lower()
            match tipo:
                case "utilitario":
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                    b = True
                    while b:
                        try:
                            nuevo_auto = Utilitario(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(),int(input("Ingrese la carga máxima del vehículo: ")), id)
                            n=False
                            self.agregar(nuevo_auto)
                            print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                            return n
                        except ValueError:
                            print("El valor ingresado no es válido, intente nuevamente")
                case "deportivo":
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    id = marca[0:3].upper() + "-" +modelo[0:2].lower()+ "_" + i
                    b = True
                    while b:
                        try:
                            nuevo_auto = Deportivo(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(), int(input("Ingrese la velocidad máxima del vehículo: ")), id)
                            n=False
                            self.agregar(nuevo_auto)
                            print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                            return n
                        except ValueError:
                            print("El valor ingresado no es válido, intente nuevamente")
                case "electrico":
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                    b = True
                    while b:
                        try:
                            nuevo_auto = Electrico(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tiempo de carga del vehículo: ")), id)
                            n=False
                            self.agregar(nuevo_auto)
                            print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                            return n
                        except:
                            print("Dato ingresado no valido, intente nuevamente")
                case "van":
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                    b = True
                    while b:
                        try:
                            nuevo_auto = Van(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese la cantidad de asientos del vehículo: ")), id)
                            n=False
                            self.agregar(nuevo_auto)
                            print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                            return n
                        except:
                            print("Dato ingresado no valido, intente nuevamente")
                case "compacto":
                    marca = input("Ingrese la marca del vehículo: ")
                    modelo = input("Ingrese el modelo del vehículo: ")
                    id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                    b = True
                    while b:
                        try:
                            nuevo_auto = Compacto(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tamaño del baul del vehículo: ")), id)
                            n=False
                            self.agregar(nuevo_auto)
                            print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                            return n
                        except:
                            print("Dato ingresado no valido, intente nuevamente")
                case _:
                    print("Tipo de vehículo no válido")
    def numero_id(self):
# Devuelve el siguiente número de ID disponible para un nuevo vehículo en el stock.
        try:
            i = self.ultimo_nodo().vehiculo.id
            i = i.split("_")[1]
            i=int(i) + 1
            i = str(i)
        except AttributeError:
            i = 0
            i = str(i)
        return i
