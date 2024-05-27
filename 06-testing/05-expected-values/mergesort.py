def split_in_two(ns):
    mid = len(ns) // 2
    return (ns[:mid], ns[mid:])


def merge_sorted(left, right):
    result = []
    i = 0
    j = 0
    left.sort()
    right.sort()
    while i != len(left) and j != len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(ns):
    sorted_left, sorted_right = split_in_two(ns)
    return merge_sorted(sorted_left, sorted_right)