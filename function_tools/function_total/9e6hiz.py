def count_non_multiples(n: int, multiples: list[int]) -> int:
    from math import gcd
    from itertools import combinations
    
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    
    count = n
    for i in range(1, len(multiples) + 1):
        for combo in combinations(multiples, i):
            m = combo[0]
            for num in combo[1:]:
                m = lcm(m, num)
            count -= (-1) ** (i + 1) * (n // m)
    return count
