import unittest
import classes_equivalencia

class TestClassesEquivalencia(unittest.TestCase):
    def test_add1(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[0], delta=5, second=-5)
    def test_add2(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[1], delta=5, second=5)
    def test_add3(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[2], delta=5, second=15)

class TestClassesEquivalencia2(unittest.TestCase):
    def test_add1(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[0], delta=5, second=-5)
    def test_add2(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[1], delta=5, second=5)
    def test_add3(self):
        self.assertAlmostEqual(first=classes_equivalencia.generate_test_cases(0, 9)[2], delta=5, second=15)


if __name__ == '__main__':
    unittest.main()
