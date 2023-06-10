from datetime import *
from random import *
from matplotlib import pyplot as plt
import numpy as np
from Vehiculos import *
from Stock import *
# validaciones
def lista_a_lista_listaentrelazada(lista, Nodo):
    if not lista:
        return None
    head = Nodo(lista[0])
    current = head
    for i in range(1, len(lista)):
        current.next = Nodo(lista[i])
        current = current.next
    return head

def validar_dni(dni):
    if 8 < len(dni)  or  len(dni )< 7 :
        return False
    if not dni.isdigit():
        return False
    return True

def validar_email(email):
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
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.isalpha() for c in password):
        return False
    return True

def validar_nombre(nombre):
    if  any(c.isdigit() for c in nombre):
        return False
    partes = nombre.split(" ")
    if len(partes) < 2:
        return False
    return True
    
    archivo.close()
    print(f"Stock guardado en el archivo {nombre_archivo}")
def numero_id(descargar):
    try:
        i = descargar
        i = i.ultimo_nodo().vehiculo.id
        i = i.split("_")[1]
        i=int(i) + 1
        i = str(i)
    except AttributeError:
        i = 0
        i = str(i)
    return i

def agregar_vehiculo_tipo(n, lista_entrelazada,i):
    l = True
    while l:
        tipo= input("Ingrese el tipo de vehículo que desea agregar: ")
        tipo=tipo.lower()
        match tipo:
            case "utilitario":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Utilitario(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(),int(input("Ingrese la carga máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "deportivo":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].lower()+ "_" + i
                nuevo_auto = Deportivo(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: ").lower(), int(input("Ingrese la velocidad máxima del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "electrico":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Electrico(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tiempo de carga del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "van":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Van(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese la cantidad de asientos del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case "compacto":
                marca = input("Ingrese la marca del vehículo: ")
                modelo = input("Ingrese el modelo del vehículo: ")
                id = marca[0:3].upper() + "-" +modelo[0:2].upper()+ "_" + i
                nuevo_auto = Compacto(marca.lower(), modelo.lower(), int(input("Ingrese el precio del vehículo: ")), int(input("Ingrese la autonomía del vehículo: ")), input("Ingrese el uso del vehículo: "), int(input("Ingrese el tamaño del baul del vehículo: ")), id)
                n=False
                lista_entrelazada.agregar(nuevo_auto)
                print(f"Se agregó el vehículo {str(nuevo_auto)} al stock")
                return n
            case _:
                print("Tipo de vehículo no válido")

def comprar_vehiculo(vehiculos_filtrados, lista, usuario):
    n=False
    archivo=open("ventas.txt", "a")
    fecha_hora = datetime.now().date()
    while n==False:
        marca_vehiculo=input("Ingrese la marca del vehículo que desea comprar: ")
        modelo_vehiculo=input("Ingrese el modelo del vehículo que desea comprar: ")
        vehiculo_comprado = None
        for i in vehiculos_filtrados:
            if i.marca==marca_vehiculo and i.modelo==modelo_vehiculo:
                print("Detalle de la compra:")
                print(f"Vehículo: {marca_vehiculo} {modelo_vehiculo}")
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
                    print(f"Se compró el vehículo {marca_vehiculo} {modelo_vehiculo}")
                    actual = lista.cabeza 
                    while actual is not None:
                        if str(actual.vehiculo.marca) == marca_vehiculo and str(actual.vehiculo.modelo) == modelo_vehiculo:
                            vehiculo_comprado = actual.vehiculo
                            id = vehiculo_comprado.id
                            lista.eliminar(id)
                            dato = f"{usuario.email},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                            archivo.write(f'{dato}')
                            break
                        actual = actual.siguiente
                    guardar_stock("stock.txt",lista)
                    n=True
                    b=False
            else:
                n=True
    archivo.close()
    return vehiculos_filtrados

def descargar_lista_ventas(nombre_archivo, usuario_actual, lista):
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            contador = 0
            total = 0
            contadormarca = 0
            lista_marca = []
            lista_contador = []
            for linea in lineas:
                campos = linea.strip().split(",")
                if campos[0] == usuario_actual.dni:
                    compra = (f"Dni: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                    contador += 1
                    total += int(campos[4])
                    lista.agregar(compra)   
            archivo.close()
            
            l = True
            while l == True:
                print("Estadisticas Disponibles:")
                print(f"1. Total Compras por Marca \n2. Cantidad de Compras Realizadas \n3. Total Gastado \n4. Detalle de Compras Realizadas \n5. Volver al menú principal")
                opcion = input("Ingrese el número de la estadística que desea ver: ")
                match opcion:    
                    case "1":
                        print("Total de compras por marca")
                        lista_entrelazada1 = lista.list()
                        for i in range(len(lista_entrelazada1)):
                            marca = lista_entrelazada1[i]
                            marca = marca.split(", ")[2]
                            marca = marca.split("Marca: ")[1]
                            contadormarca = 0
                            for x in range(len(lista_entrelazada1)):
                                marca2 = lista_entrelazada1 [x]
                                marca2 = marca2.split(", ")[2]
                                marca2 = marca2.split("Marca: ")[1]
                                if marca2 == marca:
                                    contadormarca += 1
                                        
                            if marca not in lista_marca: 
                                lista_marca.append(marca.split())
                                lista_contador.append(str(contadormarca).split())
                            if marca in lista_marca:
                                pass
                                    
                        
                        fig1, ax1 = plt.subplots()        
                        labels = lista_marca
                        size = lista_contador

                        ax1.pie(size, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                        ax1.axis('equal')

                        plt.show()
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "2":
                        print(f"Usted ha realizado {contador} compra/s")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "3":
                        print(f"El total gastado es de ${total}")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "4":
                        print("------------------------------Detalle de compras realizadas------------------------------")
                        print(lista)
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                    case "5":
                        l = False
                    case _:
                        print("Opción no válida")
                        l = True
    except FileNotFoundError:
        print("No ha realizado ninguna compra")
    



def convertir_tupla_en_lista(tupla):
    lista = []
    for elemento in tupla:
        lista.append(elemento)
    return lista


def descargar_lista_ventas_estadisticas(nombre_archivo, lista):
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            compra = None
            recaudacion = 0
            contador = 0
            contadormarca = 0
            lista_marca = []
            lista_contador = []
            lista_precio = []
            lista_fecha = []
            
            for linea in lineas:
                campos = linea.strip().split(",")
                compra = (f"Mail: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                lista.agregar(compra)
                recaudacion += int(campos[4])
                contador += 1
                

        archivo.close() 
        l = True
        while l == True:
            print("opciones: ")
            print("1. Cantidad de ventas por marca")
            print("2. Recaudacion total por dia")
            print("3. Recaudacion total")
            print("4. Cantidad de autos vendidos")
            print("5. Detalle de todas las ventas")
            print("6. Clientes distintos por mes")
            print("7. Volver al menu principal")
            op = input("Ingrese la opcion que desea(numero): ")
            match op:
                case "1":

                    lista_entrelazada1 = lista.list()
                    for i in range(len(lista_entrelazada1)):
                        marca = lista_entrelazada1[i]
                        marca = marca.split(", ")[2]
                        marca = marca.split("Marca: ")[1]
                        contadormarca = 0
                        for x in range(len(lista_entrelazada1)):
                            marca2 = lista_entrelazada1 [x]
                            marca2 = marca2.split(", ")[2]
                            marca2 = marca2.split("Marca: ")[1]
                            if marca2 == marca:
                                contadormarca += 1
                            
                        if marca not in lista_marca: 
                            lista_marca.append(marca)
                            lista_contador.append(contadormarca)
                        if marca in lista_marca:
                            pass
            
                    

                    fig1, ax1 = plt.subplots()
                    labels = lista_marca
                    size = lista_contador
                    ax1.pie(size, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
                    ax1.axis('equal')

                    plt.show()

                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "2":
                    lista_entrelazada2 = lista.list()
                    for i in range(len(lista_entrelazada2)):
                        fecha = lista_entrelazada2 [i]
                        fecha = fecha.split(", ")[1]
                        fecha = fecha.split("Fecha: ")[1]
                        contadorfac = 0
                        for x in range(len(lista_entrelazada2)):
                            fecha2 = lista_entrelazada2 [x]
                            fecha2 = fecha2.split(", ")[1]
                            fecha2 = fecha2.split("Fecha: ")[1]
                            if fecha2 == fecha:
                                precio = lista_entrelazada2 [x]
                                precio = precio.split(", ")[4]
                                precio = precio.split("Precio: ")[1]
                                precio = precio.split("$")[1]
                                contadorfac += int(precio)
                        if fecha not in lista_fecha: 
                            lista_fecha.append(fecha)
                            lista_precio.append(contadorfac)
                        if fecha in lista_fecha:
                            pass
                    
                    fig, ax = plt.subplots()
                    x = lista_fecha
                    counts = lista_precio
                    ax.bar(x, counts)
                    ax.set_ylabel('Recaudación')
                    ax.set_title('Recaudación Total por Día')          
                    plt.show()
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "3":
                        print(f"La facturación total es de: ${recaudacion}")
                        inp = input("Desea ver otra estadistica(s/n): ")
                        if inp == "s":
                            l = True
                        else:
                            l = False
                case "4":
                    print(f"Se han realizado {contador} venta/s")
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "5":
                    print("Detalle de las ventas:")
                    lista_entrelazada4 = lista.list()
                    for i in range(len(lista_entrelazada4)):
                        print(lista_entrelazada4[i])
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case"6":
                    lista_dni=[]
                    lista_puntos6=[]
                    conjunto_dni={}
                    lista_puntos6=[]
                    cont_dni=0
                    n=True
                    while n:
                        mes = str(input("ingrese mes fecha de la estadistica:"))
                        while mes.isdigit() == False:
                            mes = input("ingrese un numero: ")
                        n=False
                        if int(mes)>12:
                            print("ingrese un numero entre 1-12")
                            n=True
                    lista_entrelazada6 = lista.list()

                    for i in range(0,len(lista_entrelazada6)):
                        lista_punto6=lista_entrelazada6[i].split(",")
                        lista_punto6[1]=lista_punto6[1].split("Fecha: ")[1]
                        lista_puntos6.append([lista_punto6[0],lista_punto6[1]])
                    for i in lista_puntos6:
                        fecha_mes= datetime.strptime(i[1], '%Y-%m-%d')
                        fecha_mes=fecha_mes.month
                        if mes==str(fecha_mes):

                            lista_dni.append(i[0])
                            conjunto_dni=set(lista_dni)

                    if conjunto_dni!={}:
                        for i in conjunto_dni:
                            cont_dni+=1
                        print(f"la cantidad de compradores en este mes fue {cont_dni}, y fueron:")
                        for i in conjunto_dni:
                            print(i)
                    else:
                        print("No se han hecho compras en ese mes")
                
                case "7":
                    l = False
                case _:
                    print("Dato no válido")
                    l = True
    except FileNotFoundError:
        print("No ha realizado ninguna compra")

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