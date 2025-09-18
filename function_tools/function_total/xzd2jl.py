def divisors(n: int) -> set[int]:
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            if i != n // i:
                divs.add(n // i)
    return divs
