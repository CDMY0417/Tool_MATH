def generate_modular_sequence(start: int, end: int, remainder: int):
    return [n for n in range(start, end + 1) if n % 4 == remainder]
