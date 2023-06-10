class Pregunta:
# Esta clase tiene como objetivo representar una pregunta realizada por un usuario en un sistema de preguntas y respuestas
    def __init__(self, user, pregunta, respondida=False, respuesta=None):
        self.user = user
        self.pregunta = pregunta
        self.respondida = respondida
        self.respuesta = respuesta