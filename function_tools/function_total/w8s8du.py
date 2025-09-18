def subtract_in_base(num1: int, num2: int, base: int) -> str:
    # Convert numbers to decimal
    decimal_num1 = int(str(num1), base)
    decimal_num2 = int(str(num2), base)
    
    # Perform the subtraction in decimal
    decimal_result = decimal_num1 - decimal_num2
    
    # Convert back to the original base
    result_in_base = ''
    if decimal_result == 0:
        return '0'
    while decimal_result > 0:
        result_in_base = str(decimal_result % base) + result_in_base
        decimal_result //= base
    return result_in_base
