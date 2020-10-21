import minion_game
import unittest.mock as mock


@mock.patch('minion_game.C')
def test_a_is_vowel(mock_c):
    mock_c.return_value.f_true.return_value = True
    c = minion_game.C()
    assert minion_game.is_vowel('a', c)


def test_b_is_not_vowel():
    assert not minion_game.is_vowel('b')


def test_with_babana():
    output = minion_game.minion_game('banana')
    assert output == 'Stuart 12'


def test_with_abanab():
    output = minion_game.minion_game('ananab')
    assert output == 'Kevin 12'


def test_with_empty():
    output = minion_game.minion_game('')
    assert output == 'Draw'
