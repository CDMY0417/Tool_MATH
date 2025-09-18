def multiples_in_range(start: int, end: int, multiple_of: int):
    return [n for n in range(start + 1, end) if n % multiple_of == 0]
