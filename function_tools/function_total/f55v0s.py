def find_max_sum_of_consecutive_primes(primes: list[int], num_consecutive: int, divisor: int):
    max_sum = 0
    for i in range(len(primes) - num_consecutive + 1):
        consecutive_sum = sum(primes[i:i + num_consecutive])
        if consecutive_sum % divisor == 0:
            max_sum = max(max_sum, consecutive_sum)
    return max_sum
