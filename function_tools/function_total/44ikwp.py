def final_direction_after_spin(remaining_degrees: int) -> str:
    directions = ['north', 'east', 'south', 'west']
    index = (remaining_degrees // 90) % 4
    return directions[index]
