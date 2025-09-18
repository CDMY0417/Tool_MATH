def fibonacci_sequence(n: int) -> list[int]:
    if n <= 0:
        return []
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]
