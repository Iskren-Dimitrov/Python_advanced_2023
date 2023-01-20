'''Write a program that reads students' names and their grades and adds them to the student record.
On the first line, you will receive the number of students – N. On the following N lines, you will be receiving a student's name and grade.
For each student print all his/her grades and finally his/her average grade, formatted to the second decimal point in the format: "{student's name} -> {grade1} {grade2} ... {gradeN} (avg: {average_grade})".
The order in which we print the result does not matter.
Example:
7
Peter 5.20
Mark 5.50
Peter 3.20
Mark 2.50
Alex 2.00
Mark 3.46
Alex 3.00
'''

students_name_and_grades = int(input())
dictionary_students_name_grade = {}

for students_name_grade in range(students_name_and_grades):
    students_name, grade = input().split()

    if students_name not in dictionary_students_name_grade.keys():
        dictionary_students_name_grade[students_name] = []
    dictionary_students_name_grade[students_name].append(float(grade))

for student, grade in dictionary_students_name_grade.items():
    average_grade = sum(grade) / len(grade)
    convert_grade = ' '.join(map(lambda grades: f'{grades:.2f}', grade))
    print(f"{student} -> {convert_grade} (avg: {average_grade:.2f})")
