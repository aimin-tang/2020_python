from phonebook.src.phonebook import PhoneBook

def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add('bob', '12345')
    assert '12345' == phonebook.lookup('bob')