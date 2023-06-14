from datetime import *
from matplotlib import pyplot as plt
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
    


def comprar_vehiculo(vehiculos_filtrados, lista, usuario):
    n=False
    archivo=open("ventas.txt", "a")
    fecha_hora = datetime.now().date()
    if len(vehiculos_filtrados)==0:
        print("No hay vehículos que cumplan con los filtros ingresados.")
        archivo.close()
        return
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
                            dato = f"{usuario.dni},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                            archivo.write(f'{dato}')
                            archivo.close()
                            break
                        actual = actual.siguiente
                    lista.guardar_stock("stock.txt")
                    n=True
                    b=False
                return vehiculos_filtrados
            else:
                n=True
            
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
                    compra = (f"DNI: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
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
                    lista_marca = []
                    lista_contador = []
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


def descargar_lista_ventas_estadisticas(nombre_archivo):
    lista_entrelazada = ListaEnlazada()
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
                compra = (f"DNI: {campos[0]}, Fecha: {campos[1]}, Marca: {campos[2]}, Modelo: {campos[3]}, Precio: ${campos[4]}")
                lista_entrelazada.agregar(compra)
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
            print("6. Compradores por mes")
            print("7. Ventas por marca")
            print("8. salir")
            op = input("Ingrese la opcion que desea(numero): ")
            match op:
                case "1":

                    lista_entrelazada1 = lista_entrelazada.list()
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
                    lista_entrelazada2 = lista_entrelazada.list()
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
                    # for i in range(len(counts)):
                    #     counts[i] = int(counts[i])
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
                    lista_entrelazada4 = lista_entrelazada.list()
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
                    while n==True:
                        try:
                            mes=str(int(input("ingrese mes fecha de la estadistica:")))
                            n=False
                        except ValueError:
                            print("ingrese un numero")
                        if int(mes)>12:
                            print("ingrese un numero entre 1-12")
                            n=True
                    lista_entrelazada6 = lista_entrelazada.list()

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
                    inp = input("Desea ver otra estadistica(s/n): ")
                    if inp == "s":
                        l = True
                    else:
                        l = False
                case "7":
                    
                    marcas=[]
                    datos=[]
                    lista_entrelazada7 = lista_entrelazada.list()
                    for i in range(0,len(lista_entrelazada7)):
                        lista_punto7=lista_entrelazada7[i].split(",")      
                        lista_punto7[2]=lista_punto7[2].split("Marca: ")[1]
                        marcas.append(lista_punto7[2])
                        
                        datos.append(lista_punto7[3:5])
                    diccionario = {clave: [] for clave in marcas}
                    for i in range (0,len(marcas)):
                        diccionario[marcas[i]].append(datos[i])
                    marca=input("que marca desea buscar:")
                    marca=marca.lower()
                    for i in diccionario[marca]:
                        for j in i:
                            print(j, end="")
                        print("\n")
                        
                case "8":
                    l = False
                case _:
                    print("Dato no válido")
                    l = True
    except FileNotFoundError:
        print("No ha realizado ninguna compra")

