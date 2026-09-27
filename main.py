

students = []
student = {
    "Student ID": int(input("Enter your student ID: ")),
    "First_name": input("Enter your name: "),
    "Last_name": input("Enter your last name: "),
    "Major": input("Enter your Field of study: "),
    "Semester" : int(input("Enter your semester: ")),
    "GPA" : float(input("Enter your grade point average: ")),
    "Birth" : int(input("Enter your year of birth: "))
}
students.append(student)
# print(students)

print("1.Add Student")
print("2.Show Student")
print("3.Search Student")
print("4.Delete Student")
print("5.Exit")


choice = 0
while choice != 5:
    choice = int(input("Enter your chice: "))
    if choice == 1:
        print("1.Add Student")
    elif choice == 2:
        print("2.Show Student")
    elif choice == 3:
        print("3.Search Student")
    elif choice == 4:
        print("4.Delete Student")
print("GOOD BYE!")