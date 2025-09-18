def sum_of_digits(number: int) -> int:
    return sum(int(d) for d in str(number))
