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
