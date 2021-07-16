def solution(word_1, word_2):
    if word_1 == word_2:
        return 'same'

    if word_1.lower() == word_2.lower():
        return 'case-insensitive'

    return 'different'

if __name__ == "__main__":
    word_1, word_2 = [input() for i in range(2)]
    print(solution(word_1, word_2))
