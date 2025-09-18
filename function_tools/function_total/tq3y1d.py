def subtract_value_from_set_elements(int_set: set[int], subtract_value: int) -> set[int]:
    return {x - subtract_value for x in int_set}
