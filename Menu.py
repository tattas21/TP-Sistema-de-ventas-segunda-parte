from Stock import *
def menu(registro, usuario_actual):
    if usuario_actual is None:
        print("Bienvenido")
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Salir")
        opcion = input("Ingrese una opción (el numero): ")
        return opcion
    
    elif registro.es_admin:
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
    
def menu_admin(lista_entrelazada, registro, consulta_manager, opcion):
    match opcion:
        case "1":
            lista_entrelazada.agregar_vehiculo(registro.es_admin)
            return True
        # funciona
        case "2":
            print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
            lista_entrelazada.eliminar_vehiculo()
            return True
        # Funciona
        case "3":
            print("Stock actual: ")
            print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
            lista_entrelazada.modificar_dato_vehiculo()
            return True
        # Funciona
        case "4":
            print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
            return True
        # Ver como implementar bien mathplotlib
        case "5":
            nombre_archivo = "ventas.txt"
            descargar_lista_ventas_estadisticas(nombre_archivo, lista = ListaEnlazada())
            return True
        case "6":
            consulta_manager.responder_consulta()
            return True
        # si esto no funciona estamo mal
        case "7":
            print("Gracias por usar el sistema.")
            return False
        case _:
            print("Opción inválida.")
            return True

def menu_cliente(lista_entrelazada, registro, consulta_manager, usuario_actual, opcion):
    match opcion:
        # Funciona
        case "1":
            print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
            return True
        # funciona?
        case "2":
            lista_entrelazada.descargar_stock("stock.txt", registro.es_admin)
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
                lista_filtro_1 = lista_entrelazada.buscar(marca, modelo, precio, autonomia, uso)
                for i in range(len(lista_filtro_1)):
                    lista_filtro.append(lista_filtro_1[i])
                print("Desea agregar otro filtro? (s/n)")
                if input() == "s":
                    t = True
                else:
                    t = False
            print("Vehículos encontrados:")
            for vehiculo in lista_filtro:
                print(vehiculo)
            compra.comprar_vehiculo(lista_filtro, lista_entrelazada, usuario_actual)
            return True
        # si, puede mejorar
        case "3":
            descargar_lista_ventas("ventas.txt", usuario_actual, lista = ListaEnlazada())
            return True
        # casiquesi
        case "4":
            registro.modificar_dato(usuario_actual)
            return True
        
        case "5":
            consulta_manager.menu_consulta(usuario_actual)
            return True
        case "6":
            print("Gracias por usar el sistema.")
            return False
        case _:
            print("Opción inválida.")
            return True
def menu_usuario(registro, lista_entrelazada, consulta_manager):
    usuario_actual = registro.iniciar_sesion()     
    s = True
    while s == True:
        if usuario_actual is not None:
            opcion = menu(registro, usuario_actual)
            if opcion[0] == True:
                s = menu_admin(lista_entrelazada, registro, consulta_manager, opcion[1])
            else:
                s = menu_cliente(lista_entrelazada, registro, consulta_manager, usuario_actual,opcion[1])