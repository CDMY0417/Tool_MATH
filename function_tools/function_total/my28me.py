def inclusive_exclusive_count(N: int, divisors: list[int]) -> int:
    def count_multiples(divisor):
        return N // divisor

    total = sum(count_multiples(d) for d in divisors)
    for i in range(len(divisors)):
        for j in range(i + 1, len(divisors)):
            total -= count_multiples(divisors[i] * divisors[j])
    return total
