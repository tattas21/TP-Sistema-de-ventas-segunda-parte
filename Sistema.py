from Registro_usuario import *
from Menu import *

registro = RegistroUsuarios()
usuario_actual = None  
menu = Menu()
while True:
    match menu.menu(usuario_actual):
        case "1":
            registro.registro_user()
        case "2":
            menu.menu_usuario()
        case "3":
            print("Gracias por usar el sistema.")
            exit()
        case _:
            print("Opción inválida.")


