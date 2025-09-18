def combinations_without_replacement(total_items: int, items_drawn: int) -> int:
    result = 1
    for i in range(items_drawn):
        result *= total_items - i
    return result
