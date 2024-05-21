def odd_keys_dict(dictionary):
    result = {}
    for k, v in dictionary.items():
        if k % 2 != 0:
            result[k] = v
    return result
