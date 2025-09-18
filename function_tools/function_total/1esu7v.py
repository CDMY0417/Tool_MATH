def solve_congruences(mod1: int, rem1: int, mod2: int, rem2: int) -> int:
    x = rem2
    while x % mod1 != rem1:
        x += mod2
    return x
