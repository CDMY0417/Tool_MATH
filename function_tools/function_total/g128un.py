def multiply_dicts(dict1: dict, dict2: dict) -> dict:
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
