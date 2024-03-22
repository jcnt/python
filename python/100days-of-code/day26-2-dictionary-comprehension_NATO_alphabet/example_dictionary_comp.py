import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# student_scores = {new_key:new_value for intem in list}

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

#Marci:  passed_students = {student:"passed" for student in student_scores if student_scores[f"{student}"] > 60}
# passed_students = { new_key:new_value for (key, value) in dictionary.items() }

passed_students = { student:"passed" for (student, score) in student_scores.items() if score > 60}


print(passed_students)
