def add_indices(xs):
    index_list = []
    for i in range(0, len(xs)):
        index_list.append(i)
        i += 1
    return list(zip(index_list, xs))
