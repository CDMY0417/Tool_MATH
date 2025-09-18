def alphabetic_position_of_word(word: str, alphabet: str) -> int:
    base = len(alphabet)
    position = 0
    for i, char in enumerate(word):
        position = position * base + alphabet.index(char) + 1
    return position
