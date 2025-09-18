def count_nonzero_coefficients(seq1: list, seq2: list, constant: int):
    # Count non-zero elements in the sequences
    count = sum(1 for x in seq1 if x != 0)
    count += sum(1 for x in seq2 if x != 0)
    # Add the non-zero constant if it's non-zero
    if constant != 0:
        count += 1
    return count
