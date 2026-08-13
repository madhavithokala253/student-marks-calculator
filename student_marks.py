student_name = input("Enter student name: ")

python_marks = int(input("Enter Python marks: "))
sql_marks = int(input("Enter SQL marks: "))
dbms_marks = int(input("Enter DBMS marks: "))

total = python_marks + sql_marks + dbms_marks
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

if python_marks >= 40 and sql_marks >= 40 and dbms_marks >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("\n----- Student Result -----")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
print("Result:", result)