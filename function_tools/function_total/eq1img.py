def sum_fractions(a_num: int, a_denom: int, b_num: int, b_denom: int):
    common_denom = a_denom * b_denom
    num = a_num * b_denom + b_num * a_denom
    return num, common_denom
