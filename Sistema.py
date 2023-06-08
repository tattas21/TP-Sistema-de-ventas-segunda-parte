from Biblioteca import *
from Clases import *
from getpass import *

registro = RegistroUsuarios()
usuario_actual = None  
lista_entrelazada = ListaEnlazada()
# compra = Compra(Usuario, Vehiculo, datetime)
consulta_manager = ConsultaManager()
while True:
    print("Bienvenido")
    print("1. Registro")
    print("2. Inicio de sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción (el numero): ")
    match opcion:
        # Agregar validaciones
        case "1":
            registro.registro_user()
        case "2":
            usuario_actual = registro.iniciar_sesion()
            print(f'Bienvenido {usuario_actual.nombre}')     
            s = True
            while s == True:
                if usuario_actual is not None:
                    if registro.es_admin:
                        print('1. Agregar vehiculo')
                        print('2. Eliminar vehiculo')
                        print('3. Modificar vehiculo')
                        print('4. Ver stcok')
                        print('5. Ver ventas')
                        print('6. Responder soporte tecnico')
                        print('7. cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona
                            case "1":
                                i = numero_id(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
                                n = True 
                                while n == True:
                                    agregar_vehiculo_tipo(n, lista_entrelazada.descargar_stock("stock.txt", registro.es_admin), str(i))
                                    if input("¿Desea agregar otro vehículo? (s/n): ") == "s":
                                        i = int(i) + 1
                                        n = True
                                    else:
                                        n = False
                                lista_entrelazada.guardar_stock("stock.txt")
                            # funciona
                            case "2":
                                print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
                                id = input("Ingrese el id del vehiculo a eliminar: ")
                                actual = lista_entrelazada.cabeza 
                                while actual is not None:
                                    if actual.vehiculo.id == id:
                                        lista_entrelazada.eliminar(id)
                                        print(f"El vehiculo {actual.vehiculo.marca} {actual.vehiculo.modelo} con ID: {actual.vehiculo.id} fue eliminado.")
                                        lista_entrelazada.guardar_stock("stock.txt")
                                        break
                                    actual = actual.siguiente
                            # Funciona
                            case "3":
                                print("Stock actual: ")
                                print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
                                n = True
                                while n == True:
                                    id = input("Ingrese el id del vehiculo a modificar: ")
                                    dato = input("Ingrese el dato a modificar: ")
                                    nuevo_dato = input("Ingrese el nuevo dato: ")
                                    lista_entrelazada.modificar(id, dato, nuevo_dato)
                                    print("Desea modificar otro dato? (s/n)")
                                    if input() == "s":
                                        n = True
                                    else:
                                        n = False
                                lista_entrelazada.guardar_stock("stock.txt")
                                                                
                            # Funciona
                            case "4":
                                print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
                            # Ver como implementar bien mathplotlib
                            case "5":
                                nombre_archivo = "ventas.txt"
                                descargar_lista_ventas_estadisticas(nombre_archivo)
                            case "6":
                                consulta_manager.responder_consulta()
                            # si esto no funciona estamo mal
                            case "7":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")
                    else:
                        print('1. Ver stock')
                        print('2. Comprar vehiculo')
                        print('3. Ver mis compras')
                        print('4. Modificar mis datos')
                        print('5. Soporte Tecnico')
                        print('6. Cerrar sesion')
                        opcion = input("Ingrese una opción (el numero): ")
                        match opcion:
                            # Funciona
                            case "1":
                                print(lista_entrelazada.descargar_stock("stock.txt", registro.es_admin))
                            # funciona?
                            case "2":
                                nombre_archivo = "stock.txt"
                                lista_entrelazada = lista_entrelazada.descargar_stock("stock.txt", registro.es_admin)
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
                            # si, puede mejorar
                            case "3":
                                nombre_archivo = "ventas.txt"
                                lista = descargar_lista_ventas(nombre_archivo, usuario_actual)
                            # casiquesi
                            case "4":
                                nombre_archivo = "usuarios.txt"
                                lista_entrelazada = []
                                try:
                                    with open(nombre_archivo, "r") as archivo:
                                        lineas = archivo.readlines()
                                        for linea in lineas:
                                            campos = linea.strip().split(",")
                                            lista_entrelazada.append(campos)
                                    archivo.close()
                                except FileNotFoundError:
                                    print("No se encontró el archivo.")
                                print("1. Modificar nombre")
                                print("2. Modificar contraseña")
                                print("3. Salir")
                                opcion = input("Ingrese una opción (el numero): ")
                                match opcion:
                                    case "1":
                                        nombre = input("Ingrese nueva nombre: ")
                                        for i in range(len(lista_entrelazada)):
                                            if lista_entrelazada[i][2] == usuario_actual.email:
                                                lista_entrelazada[i][0] = nombre
                                    case "2":
                                        password = getpass("Ingrese su contraseña: ")
                                        password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                                        while not validar_password(password) or password != password_verificacion:
                                            print("Contraseña no válida.")
                                            password = getpass("Ingrese su contraseña: ")
                                            password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
                                        for i in range(len(lista_entrelazada)):
                                            if lista_entrelazada[i][2] == usuario_actual.email:
                                                lista_entrelazada[i][3] = password
                                    case "3":
                                        break
                                    case _:
                                        print("Opción inválida.")
                                with open(nombre_archivo, "w") as archivo:
                                    for i in range(len(lista_entrelazada)): 
                                        archivo.write(f"{lista_entrelazada[i][0]},{lista_entrelazada[i][1]},{lista_entrelazada[i][2]},{lista_entrelazada[i][3]}\n")
                                archivo.close()



                            case "5":
                                print('Menu de soporte tecnico')
                                print('1. Hacer una consulta')
                                print('2. Ver mis consultas')
                                print('3. Salir')
                                opcion = input("Ingrese una opción (el numero): ")
                                match opcion:
                                    case "1":
                                        consulta_manager.hacer_consulta(usuario_actual.dni, input("Ingrese su consulta: "))
                                    case "2":
                                        consulta_manager.cargar_consultas()
                                        consulta_manager.obtener_preguntas(usuario_actual.dni)
                                    case "3":
                                        break
                            case "6":
                                print("Gracias por usar el sistema.")
                                s = False
                            case _:
                                print("Opción inválida.")

        case "3":
            print("Gracias por usar el sistema.")
            exit()
        case _:
            print("Opción inválida.")


