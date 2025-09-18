def count_specific_digit_numbers(start: int, end: int, digit: str, positions: list[int]) -> int:
    count = 0
    for num in range(start, end + 1):
        num_str = str(num)
        if all(num_str[pos] == digit for pos in positions):
            count += 1
    return count
