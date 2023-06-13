class Alumno:

    def __init__(self, nombre="", turno="", correo=""):
        self.nombre = nombre
        self.turno = turno
        self.correo = correo
        self.nota = None

    def __str__(self):
        return f"{self.nombre}-{self.turno}-{self.correo} {self.nota}"

    def setNota(self, nueva_nota):
        self.nota = nueva_nota

    def convocarExamen(self):
        if self.nota >= 5:
            print(f"{self.correo}- {self.nombre} - {self.nota}convocado")
            print()