def vieta_product(real_part_1: float, imaginary_part_1: float, real_part_2: float, imaginary_part_2: float):
    real_product = real_part_1 * real_part_2 - imaginary_part_1 * imaginary_part_2
    imaginary_product = real_part_1 * imaginary_part_2 + imaginary_part_1 * real_part_2
    return real_product, imaginary_product
