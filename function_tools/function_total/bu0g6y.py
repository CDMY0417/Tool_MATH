def arrangements_excluding_position(total_spots: int, excluded_spots: int, identical_count: int):
    return (total_spots - excluded_spots) * (total_spots - 1) // identical_count
