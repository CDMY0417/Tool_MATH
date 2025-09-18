def possible_distances(max_dx: int, max_dy: int) -> list:
    distances = set()
    for dx in range(max_dx + 1):
        for dy in range(max_dy + 1):
            if dx != 0 or dy != 0:
                distances.add((dx**2 + dy**2) ** 0.5)
    return sorted(distances, reverse=True)
