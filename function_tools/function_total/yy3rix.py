def modulo_individual_sum(numbers: list[int], divisor: int) -> int:
    return sum(n % divisor for n in numbers)
