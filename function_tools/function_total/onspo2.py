def digits_count(number: int) -> tuple:
    even_count = sum(1 for digit in str(number) if int(digit) % 2 == 0)
    odd_count = sum(1 for digit in str(number) if int(digit) % 2 != 0)
    return even_count, odd_count
