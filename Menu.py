from Stock import *
from Biblioteca import *
from Registro_usuario import *
from ConsultaManager import *


class Menu:
# La clase "Menu" tiene como objetivo principal gestionar y mostrar un menú de opciones para los usuarios de un sistema.
    def __init__(self):
        self.lista_entrelazada = Stock()
        self.registro = RegistroUsuarios()
        self.consulta_manager = ConsultaManager()


    def menu_usuario(self):
# Es el método principal del menú. Permite a los usuarios iniciar sesión y 
# acceder a las opciones correspondientes según su tipo (administrador o cliente).
        usuario_actual = self.registro.iniciar_sesion()     
        s = True
        while s == True:
            if usuario_actual is not None:
                opcion = self.menu(usuario_actual)
                if opcion[0] == True:
                    s = self.menu_admin(opcion[1], usuario_actual)
                else:
                    s = self.menu_cliente(usuario_actual, opcion[1])


    def menu(self, usuario_actual):
# Muestra el menú de opciones correspondiente según el tipo de usuario. 
# Si el usuario no ha iniciado sesión, muestra las opciones de registro e inicio de sesión. 
# Si el usuario es administrador, muestra las opciones relacionadas con la gestión del sistema. 
# Si el usuario es cliente, muestra las opciones relacionadas con la compra y gestión de vehículos.
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
            print('7. Modificar datos')
            print('8. cerrar sesion')
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

    def menu_admin(self, opcion, usuario_actual):
# Procesa la opción seleccionada por un administrador y ejecuta la acción correspondiente. 
# Las acciones incluyen agregar vehículo, eliminar vehículo, modificar vehículo, ver stock, ver ventas y responder soporte técnico.
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
                usuario_actual.descargar_lista_ventas_estadisticas("ventas.txt")
                return True
            case "6":
                self.consulta_manager.responder_consulta()
                return True
            case "7":
                self.registro.modificar_dato(usuario_actual)
                return True
            case "8":
                self.registro.vaciar_usuarios()
                print("Gracias por usar el sistema.")
                return False
            case _:
                print("Opción inválida.")
                return True

    def menu_cliente(self, usuario_actual, opcion):
# Procesa la opción seleccionada por un cliente y ejecuta la acción correspondiente. 
# Las acciones incluyen ver stock, comprar vehículo, ver mis compras, modificar mis datos, soporte técnico.
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
                comprar_vehiculo(self.lista_entrelazada, usuario_actual, self.registro)
                return True
            case "3":
                usuario_actual.descargar_lista_ventas("ventas.txt")
                return True
            case "4":
                self.registro.modificar_dato(usuario_actual)
                return True
            case "5":
                self.consulta_manager.menu_consulta(usuario_actual)
                return True
            case "6":
                self.registro.vaciar_usuarios()
                print("Gracias por usar el sistema.")
                return False
            case _:
                print("Opción inválida.")
                return True