def sum_of_squares_of_digits(number: int, target_sum: int) -> bool:
    return sum(int(digit) ** 2 for digit in str(number)) == target_sum
