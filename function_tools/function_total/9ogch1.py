def count_integers_with_tens_digit(digit: int, start: int, end: int):
    count = 0
    for number in range(start, end + 1):
        if number // 10 == digit:
            count += 1
    return count
