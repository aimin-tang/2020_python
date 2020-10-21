from collections import defaultdict


def is_vowel(letter):
    if letter.lower() in list('aeiou'):
        return True
    else:
        return False


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

    return output


if __name__ == '__main__':
    s = 'BANANA'
    print(partial_score('ba', 0, 'Stuart'))
    print(partial_score('ba', 1, 'Kevin'))
    minion_game(s)
