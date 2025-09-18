def product_of_signs(signs: list[str]) -> str:
    negative_count = signs.count('-')
    if negative_count % 2 == 1:
        return '-'
    else:
        return '+' if '0' not in signs else '0'
