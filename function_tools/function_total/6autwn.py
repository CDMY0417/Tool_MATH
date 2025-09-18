def factor_out_perfect_square(n: int) -> (int, int):
    factor = 1
    for i in range(2, int(n**0.5) + 1):
        while n % (i * i) == 0:
            n //= (i * i)
            factor *= i
    return factor, n
