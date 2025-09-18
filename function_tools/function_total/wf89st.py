def even_multiples_up_to(multiple: int, max_value: int) -> list:
    return [i for i in range(multiple, max_value + 1, multiple) if i % 2 == 0]
