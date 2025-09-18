def fraction_to_mixed_number(a: int, b: int) -> str:
    whole_part = a // b
    remainder = a % b
    if remainder:
        return f"{whole_part} {remainder}/{b}"
    else:
        return str(whole_part)
