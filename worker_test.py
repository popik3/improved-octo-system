
import unittest

from worker import Employee

class TestEmployee(unittest.TestCase):
    """
    Ввод нужных значений
    """
    def setUp(self):
        self.employee = Employee("Ivan", "Ivanov", 50000, 5000)
    """
    проверка введённых значений на True
    """

    def test_init(self):
        self.assertEqual(self.employee.first_name, "Ivanov")
        self.assertEqual(self.employee.name, "Ivan")
        self.assertEqual(self.employee.annul_salary, 55000)

    def test_information_of_worker(self):
        self.employee.information_of_worker()
        # Для проверки вывода можно использовать mock или assert output, но здесь мы просто вызываем метод

if __name__ == "__main__":
    unittest.main()