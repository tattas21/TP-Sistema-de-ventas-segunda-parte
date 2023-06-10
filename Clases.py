from getpass import *
from Biblioteca import *
from datetime import *


class Compra():

    def __init__(self, Usuario, Vehiculo, fecha):
        self.usuario = Usuario
        self.vehiculo = Vehiculo
        self.fecha = fecha
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
                                dato = f"{usuario.dni},{fecha_hora},{vehiculo_comprado.marca},{vehiculo_comprado.modelo},{vehiculo_comprado.precio}\n"
                                archivo.write(f'{dato}')
                                break
                            actual = actual.siguiente
                        lista.guardar_stock("stock.txt",lista)
                        n=True
                        b=False
                else:
                    n=True
        archivo.close()


