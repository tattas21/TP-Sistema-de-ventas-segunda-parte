from Stock import *
from Biblioteca import *
from Registro_usuario import *
from ConsultaManager import *

class Menu:
    def __init__(self):
        self.lista_entrelazada = Stock()
        self.registro = RegistroUsuarios()
        self.consulta_manager = ConsultaManager()

    def menu_usuario(self):
        usuario_actual = self.registro.iniciar_sesion()     
        s = True
        while s == True:
            if usuario_actual is not None:
                opcion = self.menu(usuario_actual)
                if opcion[0] == True:
                    s = self.menu_admin(opcion[1])
                else:
                    s = self.menu_cliente(usuario_actual, opcion[1])

    def menu(self, usuario_actual):
        if usuario_actual is None:
            print("Bienvenido")
            print("1. Registro")
            print("2. Inicio de sesión")
            print("3. Salir")
            opcion = input("Ingrese una opción (el numero): ")
            return opcion
        
        elif self.registro.es_admin:
            print('1. Agregar vehiculo')
            print('2. Eliminar vehiculo')
            print('3. Modificar vehiculo')
            print('4. Ver stcok')
            print('5. Ver ventas')
            print('6. Responder soporte tecnico')
            print('7. cerrar sesion')
            op = input("Ingrese una opción (el numero): ")
            opcion = [True, op]
            return opcion
        else:
            print('1. Ver stock')
            print('2. Comprar vehiculo')
            print('3. Ver mis compras')
            print('4. Modificar mis datos')
            print('5. Soporte Tecnico')
            print('6. Cerrar sesion')
            op = input("Ingrese una opción (el numero): ")
            opcion = [False, op]
            return opcion
        
    def menu_admin(self, opcion):
        match opcion:
            case "1":
                self.lista_entrelazada.agregar_vehiculo(self.registro.es_admin)
                return True
            case "2":
                print(self.lista_entrelazada.descargar_stock("stock.txt", self.registro.es_admin))
                self.lista_entrelazada.eliminar_vehiculo()
                return True
            case "3":
                print("Stock actual: ")
                print(self.lista_entrelazada.descargar_stock("stock.txt", self.registro.es_admin))
                self.lista_entrelazada.modificar_dato_vehiculo()
                return True
            case "4":
                print(self.lista_entrelazada.descargar_stock("stock.txt", self.registro.es_admin))
                return True
            case "5":
                nombre_archivo = "ventas.txt"
                descargar_lista_ventas_estadisticas(nombre_archivo)
                return True
            case "6":
                self.consulta_manager.responder_consulta()
                return True
            case "7":
                print("Gracias por usar el sistema.")
                return False
            case _:
                print("Opción inválida.")
                return True

    def menu_cliente(self, usuario_actual, opcion):
        match opcion:
            case "1":
                self.lista_entrelazada.descargar_stock("stock.txt", self.registro.es_admin)
                
                actual = self.lista_entrelazada.cabeza
                while actual is not None:
                    actual.vehiculo.id = None
                    print(actual.vehiculo)
                    actual = actual.siguiente
                return True
            case "2":
                self.lista_entrelazada.descargar_stock("stock.txt", self.registro.es_admin)
                t = True
                lista_filtro = []
                while t == True:
                    marca = None
                    modelo = None
                    precio = None
                    autonomia = None
                    uso = None
                    buscar = input("Ingrese el dato a buscar: ")
                    match buscar:
                        case "marca":
                            marca = input("Ingrese la marca del vehiculo: ")
                            marca = marca.lower()
                        case "modelo":
                            modelo = input("Ingrese el modelo del vehiculo: ")
                            modelo = modelo.lower()
                        case "precio":
                            precio = input("Ingrese el precio del vehiculo: ")
                        case "autonomia":
                            autonomia = input("Ingrese la autonomia del vehiculo: ")
                        case "uso":
                            uso = input("Ingrese el uso del vehiculo: ")
                            uso = uso.lower()
                    lista_filtro_1 = self.lista_entrelazada.buscar(marca, modelo, precio, autonomia, uso)
                    for i in range(len(lista_filtro_1)):
                        lista_filtro.append(lista_filtro_1[i])
                    print("Desea agregar otro filtro? (s/n)")
                    if input() == "s":
                        t = True
                    else:
                        t = False
                print("Vehículos encontrados:")
                for vehiculo in lista_filtro:
                    v = vehiculo
                    v.id = None
                    print(v)
                comprar_vehiculo(lista_filtro, self.lista_entrelazada, usuario_actual)
                return True
            case "3":
                descargar_lista_ventas("ventas.txt", usuario_actual, lista = ListaEnlazada())
                return True
            case "4":
                self.registro.modificar_dato(usuario_actual)
                return True
            case "5":
                self.consulta_manager.menu_consulta(usuario_actual)
                return True
            case "6":
                print("Gracias por usar el sistema.")
                return False
            case _:
                print("Opción inválida.")
                return True