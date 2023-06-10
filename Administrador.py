from Usuario import*

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
#Este método verifica si el administrador tiene privilegios de administrador basándose en su dirección de correo electrónico (email). 
# Si el email termina con 'sistema.com.ar', se considera que el administrador es un administrador legítimo y se establece self.es_admin como True. 
# En caso contrario, se establece self.es_admin como False. Luego, se devuelve el valor de self.es_admin. 
        