import random

class Profesor:

    def __init__(self, nombre, nota_minima, nota_maxima):
        VALIDAR_NOTAS = {
            "min": (0.0, 4.0),
            "max": (6.0, 10.0)
        }
        def validar_nota_minima(nota_minima):
            min = VALIDAR_NOTAS["min"][0]
            max = VALIDAR_NOTAS["min"][1]                 

            if not str(nota_minima).isnumeric():
                raise Exception("LA NOTA DEBE SER UN NUMERO")
            if nota_minima < min:
                raise Exception(f"LA NOTA MINIMA DEBE SER SUPERIOR A{min}")
            if nota_minima > max:
                raise Exception(f"LA NOTA MINIMA DEBE SER INFERIOR A {max}")
            return nota_minima

        def validar_nota_maxima(nota_maxima):
            
            min = VALIDAR_NOTAS["max"][0]
            max = VALIDAR_NOTAS["max"][1] 

            if not str(nota_maxima).isnumeric():
                raise Exception(f"debe ser un número")
            
            if nota_maxima < min:
                raise Exception(f"")
            if nota_maxima > max:
                raise Exception(f"")
            return nota_maxima 
         
        self.nombre = nombre
        self.nota_minima = validar_nota_minima(nota_minima)
        self.nota_maxima = validar_nota_maxima(nota_maxima)
        self.profesores = list()

    def __str__(self) -> str:
        return f"{self.nombre} [{self.nota_minima}/{self.nota_maxima}]"

    def generar_nota(self) -> float:
        return random.uniform(self.nota_minima, self.nota_maxima)