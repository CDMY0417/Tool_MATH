def add_complex_numbers(num1: tuple[float, float], num2: tuple[float, float]) -> tuple[float, float]:
    real_part = num1[0] + num2[0]
    imaginary_part = num1[1] + num2[1]
    return (real_part, imaginary_part)
