
def evaluar_asignatura(calificacion):
   if calificacion < 70:
     return "Reprobado"
   else:
     return "Aprobado"

class Student:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        if len(self.courses) < 2:
            self.courses.append(course)
        else:
            raise Exception("No se puede retirar más de 2 asignaturas")





