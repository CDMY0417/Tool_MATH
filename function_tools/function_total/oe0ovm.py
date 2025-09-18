def divisors(n: int) -> list:
    divs = [i for i in range(1, n + 1) if n % i == 0]
    return divs
