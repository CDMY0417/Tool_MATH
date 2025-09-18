def fraction_to_mixed_number(fraction: tuple):
    whole_number = fraction[0] // fraction[1]
    remainder = fraction[0] % fraction[1]
    return (whole_number, (remainder, fraction[1]))
