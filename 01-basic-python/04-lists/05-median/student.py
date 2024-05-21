def median(ns):
    sorted_ns = sorted(ns)
    mid = len(sorted_ns)//2
    if len(sorted_ns) % 2 == 0:
        return (sorted_ns[mid-1] + sorted_ns[mid]) / 2
    else:
        return sorted_ns[mid]
