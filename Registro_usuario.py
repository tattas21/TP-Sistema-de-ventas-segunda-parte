from Usuario import *
from getpass import *
from Biblioteca import *

class RegistroUsuarios(Usuario):
# Esta clase administra la lista de usuarios registrados en el sistema, permite registrar nuevos usuarios, 
# iniciar sesión, modificar los datos de un usuario y guardar los usuarios en un archivo.
    def __init__(self):
        self.usuarios = []
        self.archivo = "usuarios.txt"
        self.usuario_actual = None
        self.email = None
        self.password = None
        self.es_admin = False
        self.nombre = None
        self.dni = None
        
    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email} {self.password}"
    
    def registrar_usuario(self, usuario):
# Este método recibe un objeto usuario y lo agrega a la lista de usuarios del registro. 
# Luego, llama al método guardar_usuarios para guardar los usuarios en el archivo.
        self.usuarios.append(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
# Este método guarda la lista de usuarios en el archivo especificado. 
# Abre el archivo en modo escritura y recorre la lista de usuarios, escribiendo cada uno en una nueva línea en el archivo.
        
        with open(self.archivo, "w") as f:
            for usuarios in self.usuarios:
                f.write(f"{usuarios.nombre},{usuarios.dni},{usuarios.email},{usuarios.password}\n")

        f.close()

    def cargar_usuarios(self):
# Este método carga los usuarios previamente guardados en el archivo. Abre el archivo en modo lectura, 
# lee cada línea, divide la línea en campos separados por comas y crea un objeto Usuario con esos campos. 
# Luego, agrega el objeto Usuario a la lista de usuarios del registro.
        try:
            with open("usuarios.txt", "r") as f:
                for linea in f:
                    nombre, dni, email, password = linea.strip().split(",")
                    self.usuarios.append(Usuario(nombre,dni,email,password))
            f.close()
        except FileNotFoundError:
            pass
    def buscar_usuario(self, email, dni):
# Este método busca un usuario en la lista de usuarios del registro. Recorre la lista de usuarios y compara el email y 
# el DNI del usuario con los parámetros email y dni proporcionados. Si encuentra un usuario con el mismo email o DNI, 
# muestra un mensaje de que el usuario ya existe y retorna False. Si no encuentra coincidencias, retorna None.
        for usuario in self.usuarios:
            if usuario.email == email or usuario.dni == dni:
                print(f"El usuario ya existe")
                return False
        return None
    
    def registro_user(self):
# Este método guía al usuario a través del proceso de registro. Solicita al usuario que ingrese su nombre, DNI, email y contraseña, y 
# valida cada campo utilizando las funciones validar_nombre, validar_dni, validar_email y validar_password. 
# Luego, crea un objeto Usuario con los datos ingresados y lo registra utilizando el método registrar_usuario.
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
# Este método guía al usuario a través del proceso de inicio de sesión. Solicita al usuario que ingrese su email y contraseña, 
# y verifica si coinciden con un usuario registrado. Si la combinación de email y contraseña es correcta, 
# inicia sesión y guarda el usuario actual. Si no es correcta, muestra un mensaje de error y da la opción de salir del programa.
        self.cargar_usuarios()
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
                    l = True
                    break
        
            if l == True:
                if validar_email(email)=='sistema.com.ar':
                    codigoadmin = input("Ingrese el codigo de administrador: ")
                    while codigoadmin != '1234':
                        print("Codigo de administrador no válido.")
                        codigoadmin = input("Ingrese el codigo de administrador: ")
                    self.es_admin = True       
                    n = False
                else:
                    n = False
                    self.es_admin = False
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
        print(f'Bienvenido {usuario.nombre}')
        return usuario
    
    def modificar_dato (self,usuario):
# Este método permite al usuario modificar sus datos registrados. Permite al usuario seleccionar qué dato desea modificar 
# (nombre, email o contraseña) o en caso de ser admin (contraseña) y solicita el nuevo valor para ese dato. Luego, actualiza el valor correspondiente en el objeto usuario 
# y guarda los cambios en el archivo utilizando el método guardar_usuarios.
        if self.es_admin == True:
            print("1. Modificar contraseña")
            print("2. Salir")
            n=False
            while n==False:
                dato=input("Ingrese el dato que desea modificar(NUMERO): ")
                dato=dato.lower()
                match dato:
                    case "1":
                        usuario.password = input("Ingrese la nueva contraseña: ")
                        n=True
                        while validar_password(usuario.password) == False:
                            print("Contraseña no válida.")
                            usuario.password = input("Ingrese su contraseña: ")
                        for usuarios in self.usuarios:
                            if usuarios.dni == usuario.dni:
                                usuarios.password = usuario.password
                    case "2":
                        n=True
                        pass
                    case _:
                        print("Dato no válido")
                        n == False
        else:
            print("1. Modificar nombre")
            print("2. Modificar email")
            print("3. Modificar contraseña")
            print("4. Salir")
            n=False
            while n==False:
                dato=input("Ingrese el dato que desea modificar(NUMERO): ")
                dato=dato.lower()
                match dato:
                    case "1":
                        usuario.nombre=input("Ingrese el nuevo nombre: ")
                        n=True
                        while validar_nombre(usuario.nombre) == False:
                            print("Nombre no válido.")
                            usuario.nombre = input("Ingrese su nombre: ")
                        for usuarios in self.usuarios:
                            if usuarios.dni == usuario.dni:
                                usuarios.nombre = usuario.nombre
                    case "2":
                        usuario.email=input("Ingrese el nuevo email: ")
                        n=True
                        while validar_email(usuario.email) == False:
                            print("Email no válido.")
                            usuario.email = input("Ingrese su email: ")
                        for usuarios in self.usuarios:
                            if usuarios.dni == usuario.dni:
                                usuarios.email = usuario.email
                    case "3":
                        usuario.contraseña = input("Ingrese la nueva contraseña: ")
                        n=True
                        while validar_password(usuario.contraseña) == False:
                            print("Contraseña no válida.")
                            usuario.contraseña = input("Ingrese su contraseña: ")
                        for usuarios in self.usuarios:
                            if usuarios.dni == usuario.dni:
                                usuarios.password = usuario.contraseña
                    case "4":
                        n=True
                    case _:
                        print("Dato no válido")
                        n == False
        self.guardar_usuarios()
    
    def vaciar_usuarios(self):
            self.usuarios = []