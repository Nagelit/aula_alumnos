from alumno import Alumno
from aula import Aula
from profesor import Profesor

CANT_AULAS = 5

aulas = []
for i in range(CANT_AULAS):
    aulas.append(Aula())

profesores = [
    Profesor("Juanito Balerrama", 0, 10),
    Profesor("Manolito Pomporretas", 0, 10),
    Profesor("Teres Rabal", 0, 10),
]

alumnos = [
    Alumno("Pepito", "A", "pepito@a.com"),
    Alumno("Lucia", "A", "lucia@a.com"),
    Alumno("Martita", "A", "martita@b.com"),
    Alumno("Juanito", "A", "juanito@c.com"),
    Alumno("Jorgito", "A", "jorgito@c.com"),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno(),
    Alumno()
]

aulas[0].set_profesor(profesores[0])
aulas[1].set_profesor(profesores[1])
aulas[2].set_profesor(profesores[2])
aulas[4].set_profesor(profesores[0])

contador = 0
while contador < len(alumnos):
    aulas[contador % (len(aulas) - 1)].add(alumnos[contador])
    contador += 1

contador = 0
for aula in aulas:
    print(f"AULA {contador} ----------------------------- ")

    try:
        aula.puntuar()
    except Exception as e:
        print(e)

    try:
        aula.convocar_examen("A")
    except Exception as e:
        aula.listar()
        print(e)

    print("\n" * 3)
    contador += 1
