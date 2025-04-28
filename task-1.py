student = {'alice':34, 'radha':89,'jennie':69,'kai':98,'tae':90}
student_name = input("Enter the student's name: ")

if student_name in student:
    print((f"{student_name}'s marks are: {student[student_name]}"))
else:
    print(f"Student named '{student_name}' not found ")

