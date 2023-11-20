from student import Student

# https://docs.python.org/3/library/json.html
'''
{
    "students": [
        {
            "name": "Hiromi",
            "grades": [90, 99, 53, 23],
            "id": 12344
        }, 
        {
            "name": "Igor",
            "grades": [100, 100, 78, 92],
            "id": 54321
        }
    ]
}
'''

import json

filename = 'students.json'
file = open(filename)
students = json.load(file)
student_list = []
for student in students['students']:
	student = Student(student['name'], student['grades'], student['id'])
	student_list.append(student)
	
for student in student_list:
	print(student)