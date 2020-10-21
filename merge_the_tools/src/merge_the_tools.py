def divide_string(string, k):
    result = []

    for round in range(len(string) // k):
        start_pos = k * round
        result.append(string[start_pos:start_pos + k])

    return result


def remove_duped(string):
    result = []

    for c in string:
        if c not in result:
            result.append(c)

    return ''.join(result)


def merge_the_tools(string, k):
    result = []
    for sub_string in divide_string(string, k):
        result.append(remove_duped(sub_string))

    result_s = '\n'.join(result)
    print(result_s)

    return result_s


if __name__ == '__main__':
    string, k = 'AABCAAADA', 3
    merge_the_tools(string, k)
