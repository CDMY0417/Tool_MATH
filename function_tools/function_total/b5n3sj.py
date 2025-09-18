def convert_base(num: int, from_base: int, to_base: int) -> str:
    if from_base == 10:
        n = num
    else:
        n = int(str(num), from_base)
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(int(n % to_base))
        n //= to_base
    return ''.join(str(x) for x in digits[::-1])
