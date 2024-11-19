students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
student_sorted=(sorted(students_list))


grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average = [sum(sublist) / len(sublist) for sublist in grades]

other = zip(student_sorted,average)
print(list(other))