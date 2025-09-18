def least_common_denominator(fractions: list):
    from math import gcd
    denominators = [frac.denominator for frac in fractions]
    lcd = denominators[0]
    for d in denominators[1:]:
        lcd = lcd * d // gcd(lcd, d)
    return lcd
