import unittest
from ErrorTest import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatTed_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatTed_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formated_name = get_formatted_name(
            'Wolfgang', 'Mozart', 'Amadeus')
        self.assertEqual(formated_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

