class Usuario:
    def __init__(self, nombre, dni,email, password):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.nombre} {self.dni} {self.email}"

    def __eq__(self, other):
        return self.dni == other.dni
