def sum_in_base(num1: list[int], num2: list[int], base: int) -> list[int]:
    carry = 0
    result = []
    max_len = max(len(num1), len(num2))
    num1 = [0] * (max_len - len(num1)) + num1
    num2 = [0] * (max_len - len(num2)) + num2
    for i in range(max_len - 1, -1, -1):
        total = num1[i] + num2[i] + carry
        if total >= base:
            total -= base
            carry = 1
        else:
            carry = 0
        result.append(total)
    if carry != 0:
        result.append(carry)
    return result[::-1]
