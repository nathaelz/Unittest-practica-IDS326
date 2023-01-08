from maincode import Student   # The code to test
from maincode import evaluar_asignatura
import unittest   # The test framework


class PruebasEvaluarAsignatura(unittest.TestCase):
  def test_calificacion_menor_70(self):
    resultado = evaluar_asignatura(69)
    self.assertEqual(resultado, "Reprobado")

  def test_calificacion_mayor_70(self):
    resultado = evaluar_asignatura(70)
    self.assertEqual(resultado, "Aprobado")

class TestStudent(unittest.TestCase):
    def test_add_course(self):
        student = Student()
        student.add_course("Curso 1")
        student.add_course("Curso 2")

        with self.assertRaises(Exception):
            student.add_course("Curso 3")

if __name__ == '__main__':
  unittest.main()



