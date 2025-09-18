def multiply_complex_numbers(a: int, b: int, c: int, d: int):
    real = a * c - b * d
    imaginary = a * d + b * c
    return (real, imaginary)
