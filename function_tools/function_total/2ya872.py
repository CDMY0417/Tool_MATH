def binary_sum_with_carry(digits: list[int], carry: int):
    total = sum(digits) + carry
    new_digit = total % 2
    new_carry = total // 2
    return new_digit, new_carry
