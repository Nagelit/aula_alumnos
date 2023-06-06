from alumno import Alumno
from aula import Aula
turno =["A", "B", "C"]
aula = Aula()
aula.add(Alumno("Juan", "B", "juan@o.com"))
aula.add(Alumno("Marta", "A", "marta@o.com"))
aula.add(Alumno("Alex", "A", "alex@o.com"))
aula.add(Alumno("Lucia", "B", "lucia@o.com"))

aula.listar()
turno = input("Grupo Convocado: "). upper()
aula.convocarExamen(turno)
