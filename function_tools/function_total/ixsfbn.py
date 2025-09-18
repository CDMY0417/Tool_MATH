def possible_angle_values(cos_c: float):
    import math
    angle_1 = math.degrees(math.acos(cos_c))
    angle_2 = 180 - angle_1
    return angle_1, angle_2
