def alternating_digit_sum(digits: str) -> int:
    return sum(int(d) if i % 2 == 0 else -int(d) for i, d in enumerate(digits))
