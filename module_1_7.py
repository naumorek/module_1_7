grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
midle_grades_students={}
a=students.pop()
midle_grades=sum(grades[0])/len(grades[0])
midle_grades_students.update({a:midle_grades})
a=students.pop()
midle_grades=sum(grades[1])/len(grades[1])
midle_grades_students.update({a:midle_grades})
a=students.pop()
midle_grades=sum(grades[2])/len(grades[2])
midle_grades_students.update({a:midle_grades})
a=students.pop()
midle_grades=sum(grades[3])/len(grades[3])
midle_grades_students.update({a:midle_grades})
a=students.pop()
midle_grades=sum(grades[4])/len(grades[4])
midle_grades_students.update({a:midle_grades})
print(midle_grades_students)
