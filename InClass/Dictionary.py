__author__ = 'Home'
the_students = {"x00232223":"Gisela Hernandez",
                "x00323444":"Xiaohua Xia",
                "x001344556":"Karla Hanson"}

print(the_students)
#picking info from the dictionary
the_name = (the_students["x00232223"])
print(the_name)

#checking the dictionary for validation
student_x = input('Enter X Number')
if(student_x in the_students):
    print(the_students[student_x], "is enrolled")
else:
    print(student_x, "is not enrolled")

#how to deal with KeyError
student_to_remove = input("Ender X Number to remove:")
try:
    del the_students[student_to_remove]
except KeyError:
    print(student_to_remove, "cannot be found")