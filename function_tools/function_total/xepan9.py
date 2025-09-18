def least_common_multiple(numbers: list[int]) -> int:
    from math import gcd
    lcm = numbers[0]
    for number in numbers[1:]:
        lcm = lcm * number // gcd(lcm, number)
    return lcm
