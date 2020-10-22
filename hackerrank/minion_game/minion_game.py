from collections import defaultdict


class C:
    def __init__(self):
        pass

    def f_true(self):
        return True

    def f_false(self):
        return False


def is_vowel(letter, c=None):
    c = c or C()

    if letter.lower() in list('aeiou'):
        return c.f_true()
    else:
        return c.f_false()


def scores(s):
    result = defaultdict(int)

    for start_pos in range(len(s)):
        result['Stuart'] += partial_score(s, start_pos, 'Stuart')
        result['Kevin'] += partial_score(s, start_pos, 'Kevin')

    return result


def partial_score(s, start_pos, player):
    if player.lower() == 'stuart':
        if is_vowel(s[start_pos]):
            return 0
        else:
            return len(s) - start_pos
    elif player.lower() == 'kevin':
        if not is_vowel(s[start_pos]):
            return 0
        else:
            return len(s) - start_pos
    else:
        raise ValueError(f'Unknown name: {player}')


def minion_game(string):
    # your code goes here
    result = scores(string)
    if result['Stuart'] > result['Kevin']:
        output = f"Stuart {result['Stuart']}"
    elif result['Stuart'] < result['Kevin']:
        output = f"Kevin {result['Kevin']}"
    else:
        output = 'Draw'

    print(output)

    return output


if __name__ == '__main__':
    s = 'BANANA'
    print(minion_game(s))
