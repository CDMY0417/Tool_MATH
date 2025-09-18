def is_divisible_by_11(number: int):
    digits = [int(d) for d in str(number)]
    alternating_sum = sum(digits[i] if i % 2 == 0 else -digits[i] for i in range(len(digits)))
    return alternating_sum % 11 == 0
