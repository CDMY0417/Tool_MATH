def column_sum_in_table(column_index: int, column_count: int, max_value: int) -> int:
    terms = []
    for i in range(column_index, max_value + 1, column_count):
        terms.append(i)
    return sum(terms)
