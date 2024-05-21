def create_dictionary(keys, values):
    result = {}
    for key, value in zip(keys, values):
        result[key] = value
    return result
