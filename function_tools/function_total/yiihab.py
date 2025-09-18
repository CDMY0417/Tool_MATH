def count_words_starting_with_letter(start_letter: str, word_length: int, alphabet: str) -> int:
    base = len(alphabet)
    remaining_length = word_length - 1
    position_of_letter = alphabet.index(start_letter)
    return position_of_letter * (base ** remaining_length)
