def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    words = sentence.split()
    reversed_words = words[::-1]

    result = []
    for word in reversed_words:
        result.append(swap_case(word))

    return ' '.join(result)

def swap_case(word):
    result = ""
    for letter in word:
        result += letter.swapcase()

    return result


if __name__ == '__main__':
    sentence = "rUns dOg"
    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
