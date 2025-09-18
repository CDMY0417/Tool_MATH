def count_face_cards(deck: list[str]) -> int:
    count = 0
    for card in deck:
        if card in {'jack', 'queen', 'king'}:
            count += 1
    return count
