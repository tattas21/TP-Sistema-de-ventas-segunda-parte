from Cola import *
from Usuario import *
from Pregunta import *

class ConsultaManager:
# Esta clase tiene como objetivo gestionar las consultas realizadas por los usuarios y las respuestas proporcionadas por el administrador.
    def __init__(self):
        self.consultas = Cola()

    def hacer_consulta(self, user, pregunta):
        self.cargar_consultas()
        consulta = Pregunta(user, pregunta)
        self.consultas.encolar(consulta)
        self.guardar_consultas()    
# Este método permite al usuario realizar una consulta. Carga las consultas existentes, 
# crea una nueva instancia de la clase Pregunta con los datos proporcionados, 
# encola la pregunta en la cola de consultas y guarda las consultas actualizadas en un archivo.
    def responder_consulta(self):
# Este método permite al administrador responder las consultas pendientes. Carga las consultas existentes, 
# obtiene las preguntas sin respuesta, y muestra cada pregunta para que el administrador pueda ingresar la respuesta. 
# Luego, actualiza el estado de la pregunta a respondida y guarda las consultas actualizadas en el archivo.
        self.cargar_consultas()
        preguntas_sin_respuesta = self.obtener_preguntas_sin_respuesta()
        n = True
        while n == True:
            for pregunta in preguntas_sin_respuesta:
                respuesta = input(f"Responder a la pregunta '{pregunta.pregunta}': ")
                pregunta.respuesta = respuesta
                pregunta.respondida = True
                l = input("¿Desea seguir respondiendo preguntas? (s/n) ")
                l = l.lower()
                if l == "s":
                    continue
                elif l == "n":
                    n = False
                    break
        self.guardar_consultas()
        return 

    def obtener_preguntas_sin_respuesta(self):
# Este método retornea una lista de las preguntas que no tienen respuesta.
        preguntas_sin_respuesta = []
        for consulta in self.consultas.items:
            if consulta.respondida == "False":
                preguntas_sin_respuesta.append(consulta)
        return preguntas_sin_respuesta

    def cargar_consultas(self):
# Este método carga las consultas desde un archivo de texto y las encola en la cola de consultas. 
# Cada línea del archivo representa una consulta y se descompone en los datos correspondientes.
        self.consultas.vaciar()
        try:
            with open("consultas.txt", "r") as archivo:
                for line in archivo:
                    datos = line.strip().split(",")
                    datos_user = datos[0].split(" ")
                    datos_user[0] = " ".join(datos_user[:2])
                    datos_user.remove(datos_user[1])
                    user = Usuario(*datos_user, password=None)
                    pregunta = datos[1]
                    respondida = datos[2] 
                    respuesta = datos[3] if respondida == "True" else None
                    consulta = Pregunta(user, pregunta, respondida, respuesta)
                    self.consultas.encolar(consulta)
            archivo.close()
        except FileNotFoundError:
            pass

    def guardar_consultas(self):
# Guarda las consultas en un archivo de texto. Cada consulta se guarda en una línea separada con los datos correspondientes.
        with open("consultas.txt", "w") as archivo:
            for consulta in self.consultas.items:
                archivo.write(f"{consulta.user},{consulta.pregunta},{consulta.respondida},{consulta.respuesta}\n")
        archivo.close()

    def obtener_preguntas(self, user):
# Obtiene las preguntas (con respuesta y sin respuesta) de un usuario específico (Basandose en el DNI) y las muestra por pantalla.
        preguntas_con_respuesta = []
        preguntas_sin_respuesta = []
        for consulta in self.consultas.items:
            if consulta.user == user and consulta.respondida == "True":
                preguntas_con_respuesta.append(consulta)
            if consulta.user == user and consulta.respondida == "False":
                preguntas_sin_respuesta.append(consulta)
        print("Preguntas respondidas: ")
        if preguntas_con_respuesta == []:
            print("No hay preguntas respondidas.")
        for pregunta in preguntas_con_respuesta:
            print(f"{pregunta.pregunta}: {pregunta.respuesta}")
        print("Preguntas sin responder: ")
        if preguntas_sin_respuesta == []:
            print("No hay preguntas hechas.")
        for pregunta in preguntas_sin_respuesta:
            print(f"{pregunta.pregunta}")
    def menu_consulta(self,usuario_actual):
# Muestra un menú de opciones para el usuario actual (soporte técnico).
        print('Menu de soporte tecnico')
        print('1. Hacer una consulta')
        print('2. Ver mis consultas')
        print('3. Salir')
        opcion = input("Ingrese una opción (el numero): ")
        match opcion:
            case "1":
                self.hacer_consulta(usuario_actual, input("Ingrese su consulta: "))
            case "2":
                self.cargar_consultas()
                self.obtener_preguntas(usuario_actual)
            case "3":
                return 




