import generar_nombre
class Alumno:

    def __init__(self, nombre= None, turno = "A", correo = None):
        user = generar_nombre.generar_correo_nombre()

        self.nombre = nombre if nombre is not None else user['nombre']
        self.turno = "A"
        self.correo = correo if correo is not None else user['correo']
        self.nota = 0

    def __str__(self):
        return f" - {self.nombre}\n - {self.turno}\n - {self.correo}\n - {self.nota}"

    def convocar_examen(self,turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"Turno: {turno}")
            print(f"Nombre: {self.nombre}")
            print(f"Correo: {self.correo}")
            print(f"Nota: {self.nota}")
            print(f"convocado")
    
    def setNota(self, nota):
        self.nota = nota
    