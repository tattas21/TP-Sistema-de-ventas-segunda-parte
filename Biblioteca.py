from datetime import *
from matplotlib import pyplot as plt
from Vehiculos import *
from Stock import *
# validaciones
def validar_dni(dni):
# Tiene como objetivo validar si un número de DNI es válido. Recibe como parámetro un string que representa el número de DNI. 
# La funcion verifica si la longitud del string está entre 7 y 8 caracteres y si todos los caracteres son dígitos. 
# Devuelve True si el DNI es válido y False en caso contrario.
    if 8 < len(dni)  or  len(dni )< 7 :
        return False
    if not dni.isdigit():
        return False
    return True

def validar_email(email):
# tiene como objetivo validar si una dirección de correo electrónico es válida. 
# Recibe como parámetro un string que representa la dirección de correo electrónico. 
# La funcion verifica si la dirección tiene el formato correcto, es decir, tiene una única "@" que divide el usuario del dominio, 
# el usuario y el dominio no están vacíos, el dominio tiene al menos un punto y no hay caracteres inválidos. 
# Si la dirección de correo electrónico es válida, devuelve True, y si no, devuelve False. Además, si el dominio es "sistema.com.ar", 
# devuelve el dominio en sí.
    partes = email.split('@')
    if len(partes) != 2:
        return False
    usuario = partes[0]
    dominio = partes[1]
    if not usuario or not dominio:
        return False
    if '.' not in dominio:
        return False
    if usuario[-1] == '.':
        return False
    if '..' in usuario or '..' in dominio:
        return False
    if dominio == 'sistema.com.ar':
        return dominio
    return True

def validar_password(password):
# Tiene como objetivo validar si una contraseña cumple con ciertos requisitos. 
# Recibe como parámetro un string que representa la contraseña. 
# La funcion verifica si la contraseña tiene al menos 8 caracteres, contiene al menos un dígito y al menos una letra. 
# Devuelve True si la contraseña cumple con los requisitos y False en caso contrario.
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isalpha() for c in password):
        return False
    return True

def validar_nombre(nombre):
# TTiene como objetivo validar si un nombre cumple con ciertos requisitos. 
# Recibe como parámetro un string que representa el nombre. 
# La funcion verifica si el nombre contiene al menos un dígito y tiene al menos dos partes separadas por un espacio. 
# Devuelve True si el nombre cumple con los requisitos y False en caso contrario.
    if  any(c.isdigit() for c in nombre):
        return False
    partes = nombre.split(" ")
    if len(partes) < 2:
        return False
    return True
    


def comprar_vehiculo(lista, usuario, registro):
# Recibe como parámetros una lista de vehículos filtrados, una lista enlazada que representa el stock de vehículos y un objeto usuario. 
# La funcion solicita al usuario que ingrese la marca y el modelo del vehículo que desea comprar.
# Luego, verifica si el vehículo está en la lista de vehículos filtrados. 
# Si lo encuentra, muestra los detalles de la compra y solicita la confirmación del usuario. 
# Si el usuario confirma la compra, se elimina el vehículo del stock y se guarda la información de la compra en un archivo. 
    lista.descargar_stock("stock.txt", registro.es_admin)
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
        lista_filtro_1 = lista.buscar(marca, modelo, precio, autonomia, uso)
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
    
    n=False
    archivo=open("ventas.txt", "a")
    fecha_hora = datetime.now().date()
    if len(lista_filtro)==0:
        print("No hay vehículos que cumplan con los filtros ingresados.")
        archivo.close()
        return
    while n==False:
        id_vehiculo = input("Ingrese el ID del vehículo que desea comprar: ")
        vehiculo_comprado = None
        for i in lista_filtro:
            if i.id == id_vehiculo:
                print("Detalle de la compra:")
                print(f"Vehículo: {i.marca} {i.modelo}")
                print(f"Precio: ${i.precio}")
                print(f"Transferir ${i.precio} a la siguiente cuenta:")
                print("Nombre del banco: HSBC")
                print("CBU: 0873776281914709007725")
                print("CUIT: 30-12345678-2")
                print("Razon social: ITBA CAR S.R.L")
                print("Mail: ventas@itbacar.org.ar")
                print("Cuenta: CC U$S 105-435261/0 ")
                print(f"Fecha y hora de la compra: {fecha_hora}")
                m = False
                b = True
                while m == False:
                    confirmacion = input("¿Confirma que ha realizado la transferencia? (s/n) ")
                    confirmacion = confirmacion.lower()
                    if confirmacion == "s":
                        print("Compra realizada con éxito")
                        m = True
                        continue
                    elif confirmacion == "n":
                        print("Compra cancelada")
                        m = True
                        b = False
                        n = True
                    else:
                        print("Opción no válida")
                # nuevo
                while b == True:
                    print(f"Se compró el vehículo {i.marca} {i.modelo}")
                    actual = lista.cabeza 
                    while actual is not None:
                        if str(actual.vehiculo.id) == id_vehiculo:
                            vehiculo_comprado = actual.vehiculo
                            id = vehiculo_comprado.id
                            lista.eliminar(id)
                            dato = f"{usuario.dni},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                            archivo.write(f'{dato}')
                            archivo.close()
                            break
                        actual = actual.siguiente
                    lista.guardar_stock("stock.txt")
                    n=True
                    b=False
                return lista_filtro
            else:
                n=True
            
    return lista_filtro
