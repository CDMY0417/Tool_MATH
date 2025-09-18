def sum_of_three_cubes(cubes: list[int]) -> set:
    sums = set()
    for i in cubes:
        for j in cubes:
            for k in cubes:
                sums.add(i + j + k)
    return sums
