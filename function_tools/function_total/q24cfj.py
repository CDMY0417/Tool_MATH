def rationalize_denominator(numerator: str, denominator: str) -> str:
    conjugate = denominator.replace('-', '+') if '-' in denominator else denominator.replace('+', '-')
    num = f'({numerator}) * ({conjugate})'
    denom = f'({denominator}) * ({conjugate})'
    return f'{num} / {denom}'
