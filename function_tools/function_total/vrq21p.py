def simplest_radical_form(number: int) -> tuple:
    factor = int(number ** 0.5)
    while factor > 1:
        if number % (factor**2) == 0:
            return (number // (factor**2)), factor
        factor -= 1
    return number, 1
