from Biblioteca import *
from getpass import *
from datetime import *
from Usuario import *
from Vehiculos import *
from Stock import *
from ConsultaManager import *
from Registro_usuario import *

registro = RegistroUsuarios()
usuario_actual = None  
lista_entrelazada = Stock()
consulta_manager = ConsultaManager()
while True:
    opcion = menu(registro, usuario_actual)
    match opcion:
        case "1":
            registro.registro_user()
        case "2":
            menu_usuario(registro, lista_entrelazada, consulta_manager)
        case "3":
            print("Gracias por usar el sistema.")
            exit()
        case _:
            print("Opción inválida.")


