from minion_game import minion_game

def test_with_babana():
    output = minion_game('banana')
    assert output == 'Stuart 12'

def test_with_abanab():
    output = minion_game('ananab')
    assert output == 'Kevin 12'

def test_with_empty():
    output = minion_game('')
    assert output == 'Draw'
