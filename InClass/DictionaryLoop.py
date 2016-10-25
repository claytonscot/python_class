__author__ = 'Home'
#create list
NUM_STUDENTS = 3

the_students = {}

for i in range(NUM_STUDENTS):
    student_x = input('Enter Student X Number')
    student_name = input('Enter Student Name')
    the_students[student_x] = student_name

print(the_students)

#loop through items in existing dictionary

for student_x in the_students:
    print(student_x)
