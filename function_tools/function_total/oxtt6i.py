def alternating_digit_sum(digits: list[int]) -> int:
    return sum(digits[i] if i % 2 == 0 else -digits[i] for i in range(len(digits)))
