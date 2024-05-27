def closest(points, target_point):
    return min(points, key=lambda point: ((point[0]-target_point[0])**2 + (point[1]-target_point[1])**2)**0.5)