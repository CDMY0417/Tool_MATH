def generate_numbers_with_1s_and_0s(max_digits: int):
    from itertools import product
    for digits in product('10', repeat=max_digits):
        yield int(''.join(digits))
