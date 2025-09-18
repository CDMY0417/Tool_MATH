def packing_height_crate_b(num_layers: int, initial_height: float, height_increment: float) -> float:
    return initial_height + (num_layers - 1) * height_increment
