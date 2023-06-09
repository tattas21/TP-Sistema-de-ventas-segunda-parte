from matplotlib import pyplot as plt
from Stock import *
from datetime import *

class Usuario:
# La clase "Usuario" tiene como objetivo representar un usuario con sus atributos básicos, como el nombre, DNI, email y contraseña.
    def __init__(self, nombre, dni,email, password):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email}"

    def __eq__(self, other):
# Es un método especial que se utiliza para comparar dos objetos de la clase "Usuario". 
# En este caso, compara si el DNI del objeto actual es igual al DNI del otro objeto pasado como argumento. 
# Devuelve True si son iguales y False si no lo son.
        return self.dni == other.dni
    def descargar_lista_ventas_estadisticas(self,nombre_archivo):
#tiene un propósito similar a descargar_lista_ventas, pero con algunas diferencias en las estadísticas que ofrece. Algunas de las funcionalidades que ofrece son:

# Lee el archivo especificado (nombre_archivo) que contiene la lista de ventas.
# 
# Recorre las líneas del archivo y extrae los campos relevantes de la línea (DNI, fecha, marca, modelo, precio) y 
# los agrega a una lista enlazada (lista_entrelazada).
# 
# Realiza diferentes operaciones y cálculos basados en las estadísticas de las ventas.
# 
# Muestra un menú de opciones de estadísticas disponibles.
# 
# Dependiendo de la opción seleccionada por el usuario, realiza diferentes cálculos y muestra los resultados.
# 
# En la opción "Cantidad de ventas por marca" (1), genera un gráfico de pastel que muestra la cantidad de ventas 
# realizadas por cada marca.
# 
# En la opción "Recaudacion total por dia" (2), genera un gráfico de barras que muestra la recaudación total por día.
# 
# En la opción "Recaudacion total" (3), muestra la recaudación total de todas las ventas.
# 
# En la opción "Cantidad de autos vendidos" (4), muestra la cantidad total de autos vendidos.
# 
# En la opción "Detalle de todas las ventas" (5), muestra el detalle de todas las ventas realizadas.
# 
# En la opción "Compradores por mes" (6), permite al usuario ingresar un mes y muestra la cantidad de compradores y 
# sus DNIs correspondientes en ese mes.
# 
# En la opción "Ventas por marca" (7), permite al usuario ingresar una marca y muestra el detalle de las ventas 
# correspondientes a esa marca.
# 
# En la opción "Salir" (8), finaliza el ciclo del menú y regresa al menú principal. 

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
                    case "3":
                            print(f"La facturación total es de: ${recaudacion}")
                    case "4":
                        print(f"Se han realizado {contador} venta/s")
                    case "5":
                        print("Detalle de las ventas:")
                        lista_entrelazada4 = lista_entrelazada.list()
                        for i in range(len(lista_entrelazada4)):
                            print(lista_entrelazada4[i])
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
                        try:
                            for i in diccionario[marca]:
                                for j in i:
                                    print(j, end="")
                                print("\n")
                        except KeyError:
                            print("no se encontro la marca")
                            
                    case "8":
                        l = False
                    case _:
                        print("Dato no válido")
                        l = True
        except FileNotFoundError:
            print("No ha realizado ninguna compra")
    
    def descargar_lista_ventas(self,nombre_archivo):
# Tiene como objetivo leer un archivo de ventas y realizar diferentes operaciones relacionadas con las estadísticas de las compras. 
# Algunas de las funcionalidades que ofrece son:

# Lee el archivo especificado (nombre_archivo) que contiene la lista de ventas.
# 
# Recorre las líneas del archivo y verifica si el campo del DNI coincide con el DNI del usuario actual (usuario_actual.dni).
# 
# Si hay una coincidencia, extrae los campos relevantes de la línea (fecha, marca, modelo, precio) y 
# los agrega a la lista proporcionada (lista).
# 
# Muestra un menú de opciones de estadísticas disponibles.
# 
# Dependiendo de la opción seleccionada por el usuario, realiza diferentes cálculos y muestra los resultados.
# 
# En el caso de la opción "Total Compras por Marca" (1), se genera un gráfico de pastel que muestra el 
# total de compras realizadas por cada marca.
# 
# En la opción "Cantidad de Compras Realizadas" (2), muestra la cantidad de compras realizadas por el usuario actual.
# 
# En la opción "Total Gastado" (3), muestra el total gastado en todas las compras del usuario actual.
# 
# En la opción "Detalle de Compras Realizadas" (4), muestra el detalle de todas las compras realizadas por el usuario actual.
# 
# En la opción "Volver al menú principal" (5), finaliza el ciclo del menú y regresa al menú principal.

        try:
            with open(nombre_archivo, "r") as archivo:
                lineas = archivo.readlines()
                compra = None
                contador = 0
                total = 0
                contadormarca = 0
                lista_marca = []
                lista_contador = []
                lista = ListaEnlazada()
                for linea in lineas:
                    campos = linea.strip().split(",")
                    if campos[0] == self.dni:
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
                    case "2":
                        print(f"Usted ha realizado {contador} compra/s")
                    case "3":
                        print(f"El total gastado es de ${total}")
                    case "4":
                        print("------------------------------Detalle de compras realizadas------------------------------")
                        print(lista)
                    case "5":
                        l = False
                    case _:
                        print("Opción no válida")
                        l = True
        except FileNotFoundError:
            print("No ha realizado ninguna compra")