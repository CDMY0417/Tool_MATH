def fibonacci(n: int):
    a, b = 0, 1
    fib_sequence = [a]
    for _ in range(n):
        a, b = b, a + b
        fib_sequence.append(a)
    return fib_sequence
