import unittest
from phonebook.src.phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add('Bob', '12345')
        number = self.phonebook.lookup('Bob')
        self.assertEqual(number, '12345')

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    @unittest.skip('WIP')
    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')


if __name__ == '__main__':
    unittest.main()
