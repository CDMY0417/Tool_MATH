def complete_the_square(a: int, b: int) -> tuple:
    h = b / (2 * a)
    completed = (a * (h)**2, -h)
    return completed
