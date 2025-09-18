def digit_square_ends_with(n: int, digit: int) -> bool:
    return (n * n) % 10 == digit
