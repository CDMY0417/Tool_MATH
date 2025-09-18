def product_of_numbers(nums: list[float]) -> float:
    product = 1
    for num in nums:
        product *= num
    return product
