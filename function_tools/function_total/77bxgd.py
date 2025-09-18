def simplify_square_root(n: int) -> str:
    import math
    factor = max([i for i in range(1, int(math.sqrt(n)) + 1) if n % (i * i) == 0])
    simplified = n // (factor * factor)
    return f'{factor}√{simplified}' if factor != 1 else f'√{n}'
