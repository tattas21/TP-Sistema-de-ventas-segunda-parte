from getpass import *
from Biblioteca import *
from datetime import *

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

def validar_dni(dni):
    if 8 < len(dni)  or  len(dni )< 7 :
        return False
    if not dni.isdigit():
        return False
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
    
#Clases Usuarios
# clase usuario general de esta se hereda administrador y cliente
class Usuario:
    def __init__(self, nombre, dni,email, password):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email}"


class administrador(Usuario):
    def __init__(self,nombre,dni,email,password, es_admin):
        super().__init__(nombre,dni,email,password)
        self.es_admin = None
    def es_administrador(self):
        if self.email == 'sistema.com.ar':
            self.es_admin = True
            return self.es_admin 
        else:
            self.es_admin = False
            return self.es_admin 
    


class RegistroUsuarios(Usuario):
    def __init__(self):
        self.usuarios = []
        self.archivo = "usuarios.txt"
        self.cargar_usuarios()
        self.usuario_actual = None
        self.email = None
        self.password = None
        self.es_admin = False
        self.nombre = None
        self.dni = None
        
    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email} {self.password}"
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
        with open(self.archivo, "w") as f:
            for usuario in self.usuarios:
                f.write(f"{usuario.nombre},{usuario.dni},{usuario.email},{usuario.password}\n")
        f.close()

    def cargar_usuarios(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    nombre, dni, email, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(nombre,dni,email,password))
            f.close()
        except FileNotFoundError:
            pass
    def buscar_usuario(self, email, dni):
        for usuario in self.usuarios:
            if usuario.email == email or usuario.dni == dni:
                print(f"El usuario ya existe")
                return False
        return None
    
    def registro_user(self):
        nombre = input("Ingrese su nombre: ")
        while validar_nombre(nombre) == False:
            print("Nombre no válido.")
            nombre = input("Ingrese su nombre: ")
        dni = input("Ingrese su DNI: ")
        d = None
        while validar_dni(dni) == False or self.buscar_usuario(d,dni) == False:
            print("DNI no válido.")
            dni = input("Ingrese su DNI: ")
        em = None
        email = (input("Ingrese su email: "))
        while  validar_email(email) == False or self.buscar_usuario(email,em) == False:
            print("Email no válido.")
            email = input("Ingrese su email: ")
        email=email.lower()
        # Agregue el getpass, simplemente por estetica, busque en internet alguna forma de ocultar la contraseña y me aparecio esto.
        password = getpass("Ingrese su contraseña (Debe tener al menos 8 caracteres entre esos al menos una letra o numero): ")
        password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
        while not validar_password(password) or password != password_verificacion:
            print("Contraseña no válida.")
            password = getpass("Ingrese su contraseña: ")
            password_verificacion = getpass("Ingrese su contraseña nuevamente: ")
        if validar_email(email) == 'sistema.com.ar':
            codigoadmin=input("Ingrese el codigo de administrador: ")
        usuario = Usuario(nombre, dni,email, password)
        self.registrar_usuario(usuario)
        if validar_email(email) == 'sistema.com.ar' and codigoadmin == '1234':
            print('Bienvenido administrador')
            pass
        else:    
            print("Usuario registrado correctamente.")    

    def iniciar_sesion(self):
        l = False
        email = input("Ingrese su email: ")
        email=email.lower()
        es_admin=False
        p = input("Desea ver la contraseña que ingresaste? (s)")
        match p:
            case "s":
                password = input("Ingrese su contraseña: ")
            case _:
                password = getpass("Ingrese su contraseña: ")
        n = True
        while n == True:
            for usuario in self.usuarios:
                if usuario.email == email and usuario.password == password:
                    self.nombre = usuario.nombre
                    self.dni = usuario.dni
                    self.email = usuario.email
                    self.password = usuario.password
                    self.usuario_actual = usuario
                    l = True
        
            if l == True:
                if validar_email(email)=='sistema.com.ar':
                    codigoadmin = input("Ingrese el codigo de administrador: ")
                    while codigoadmin != '1234':
                        print("Codigo de administrador no válido.")
                        codigoadmin = input("Ingrese el codigo de administrador: ")
                    self.es_admin = True       
                    usuario_actual = self.usuario_actual
                    n = False
                    
                else:
                    usuario_actual = self.usuario_actual
                    n = False
            else:
                print("Email o contraseña incorrectos.")
                salir = input("¿Desea salir del programa? (s/n): ")
                salir = salir.lower()
                if salir == "s":
                    exit()
                    
                else:
                    email = input("Ingrese su email: ")
                    email=email.lower()
                    p = input("Desea ver la contraseña que ingresaste? (s)")
                    match p:
                        case "s":
                            password = input("Ingrese su contraseña: ")
                        case _:
                            password = getpass("Ingrese su contraseña: ")
        return usuario_actual

# Ver opcion sin clase

class Vehiculo:
    def __init__(self, modelo, marca, precio,  autonomia, uso, id):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.autonomia = autonomia
        self.uso = uso
        self.id = id
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: {self.precio},Autonomia: {self.autonomia}, Uso: {self.uso}"

class Utilitario(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, carga_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.carga_maxima = carga_maxima
    def __str__(self):
        return super().__str__() + f", Carga máxima: {self.carga_maxima}, ID: {self.id}"
        
class Deportivo(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso, velocidad_maxima, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.velocidad_maxima = velocidad_maxima
    def __str__(self):
        return super().__str__() + f", Velocidad máxima: {self.velocidad_maxima}, ID: {self.id}"
        
class Electrico(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, tiempo_carga, id):
        super().__init__(modelo, marca, precio,autonomia, uso,  id)
        self.tiempo_carga = tiempo_carga
    def __str__(self):
        return super().__str__() + f", Tiempo de carga: {self.tiempo_carga}, ID: {self.id}"
        
class Van(Vehiculo):
    def __init__(self, marca, modelo, precio,autonomia, uso, asientos, id):
        super().__init__(modelo, marca, precio, autonomia, uso, id)
        self.asientos = asientos

    def __str__(self):
        return f"Tipo: Van" + super().__str__() + f", Asientos: {self.asientos}, ID: {self.id}"
        
class Compacto(Vehiculo):
    def __init__(self, marca, modelo, precio, autonomia, uso,tamaño_baul, id):
        super().__init__(modelo, marca, precio,autonomia, uso, id)
        self.tamaño_baul = tamaño_baul
    def __str__(self):
        return super().__str__() + f", Tamaño del baul: {self.tamaño_baul}, ID: {self.id}"
    

class Nodo:
    def __init__(self, vehiculo, siguiente = None):
        self.vehiculo = vehiculo
        self.siguiente = siguiente

        

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, vehiculo):
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
        lista = []
        nodo = self.cabeza
        while nodo is not None:
            lista.append(nodo.vehiculo)
            nodo = nodo.siguiente
        return lista
    def ultimo_nodo(self):
        while self.cabeza.siguiente is not None:
            self.cabeza = self.cabeza.siguiente
        return self.cabeza
    def modificar(self, id, dato, nuevo_dato):
        if self.cabeza is None:
            return
        else:
            actual = self.cabeza
            while actual is not None:
                if actual.vehiculo.id == id:
                    if dato == "marca":
                        actual.vehiculo.marca = nuevo_dato
                        return
                    elif dato == "modelo":
                        actual.vehiculo.modelo = nuevo_dato
                        return
                    elif dato == "precio":
                        actual.vehiculo.precio = nuevo_dato
                        return
                    elif dato == "autonomia":
                        actual.vehiculo.autonomia = nuevo_dato
                        return
                    elif dato == "uso":
                        actual.vehiculo.uso = nuevo_dato
                        return
                    elif dato == "carga maxima":
                        actual.vehiculo.carga_maxima = nuevo_dato
                        return
                    elif dato == "velocidad maxima":
                        actual.vehiculo.velocidad_maxima = nuevo_dato
                        return
                    elif dato == "tiempo carga":
                        actual.vehiculo.tiempo_carga = nuevo_dato
                        return
                    elif dato == "asientos":
                        actual.vehiculo.asientos = nuevo_dato
                        return
                    elif dato == "tamaño baul":
                        actual.vehiculo.tamaño_baul = nuevo_dato
                        return
                actual = actual.siguiente
            return "No se encontró el vehículo"
    def buscar(self, marca, modelo, precio, autonomia, uso):
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
        try:
            with open(nombre_archivo, "r") as archivo:
                lineas = archivo.readlines()
                vehiculo=None
                for linea in lineas:
                    campos = linea.strip().split(",")
                    if campos[0] == "utilitario":
                        if variable == True:
                            vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Utilitario(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)

                    elif campos[0] == "deportivo":
                        if variable == True:
                            vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Deportivo(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "electrico":
                        if variable == True:
                            vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Electrico(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "van":
                        if variable == True:
                            vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Van(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)
                    elif campos[0] == "compacto":
                        if variable == True:
                            vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), (campos[7]))
                        else:
                            vehiculo = Compacto(campos[1], campos[2], int(campos[3]), int(campos[4]), (campos[5]), int(campos[6]), None)

                    self.agregar(vehiculo)
            archivo.close()

        except FileNotFoundError:
            print("El archivo no existe")
        return self
    
    def guardar_stock(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            if self.cabeza is not None:
                actual = self.cabeza
                datos=None
                while actual is not None:
                    datos = str(actual.vehiculo)
                    archivo.write(f"{datos}\n")
                    actual = actual.siguiente
        archivo.close()
        print(f"Stock guardado en el archivo {nombre_archivo}")

