def rectangle_sizes(grid_width: int, grid_height: int):
    sizes = set()
    for w in range(1, grid_width + 1):
        for h in range(1, grid_height + 1):
            sizes.add((w, h))
    return list(sizes)
