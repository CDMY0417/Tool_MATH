def count_factors_of_k(n: int, k: int) -> int:
    count = 0
    for i in range(1, n+1):
        num = i
        while num % k == 0:
            num //= k
            count += 1
    return count
