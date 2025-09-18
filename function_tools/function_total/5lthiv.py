def different_suit_probability(total_suits: int, cards_per_suit: int, cards_drawn: int) -> float:
    same_suit_cards = cards_per_suit - 1
    remaining_cards = total_suits * cards_per_suit - cards_drawn
    different_suit_cards = remaining_cards - same_suit_cards
    return different_suit_cards / remaining_cards
