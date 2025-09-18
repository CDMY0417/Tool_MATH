def minimum_linear_combination(step1: int, step2: int) -> int:
    factor1, factor2 = step1, step2
    target = 0
    while True:
        target += factor2
        if target % factor1 == 0:
            return target
