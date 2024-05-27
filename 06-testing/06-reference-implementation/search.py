from student import Student

def linear_search(students, target_id):
    for student in students:
        if student.id == target_id:
            return student
    return None

def binary_search(students, target_id):
    left = 0
    right = len(students)
    while left < right:
        mid = (left + right) //2
        mid_id = students[mid].id
        if mid_id < target_id:
            left = mid + 1
        elif mid_id > target_id:
            right = mid
        else:
            return students[mid]
    return None
