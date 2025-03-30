import unittest
from city_functions import city_names

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatTed_name = city_names('janis', 'joplin')
        self.assertEqual(formatTed_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()