def divisors(n: int):
    divs = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divs.append(i)
    return divs
