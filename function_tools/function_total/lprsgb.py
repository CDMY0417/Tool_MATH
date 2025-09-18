def matrix_multiplication(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    product = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                product[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return product
