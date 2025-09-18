def arrange_two_or_fewer_digits(digits: set) -> set:
    from itertools import permutations
    one_digit = {d for d in digits}
    two_digits = {int(''.join(p)) for p in permutations(digits, 2)}
    return one_digit | two_digits
