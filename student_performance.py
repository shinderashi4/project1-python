name = input("enter your name: ")

roll_number = input("enter your roll number: ")

maths = int(input("enter your marks in maths: "))
science = int(input("enter your marks in science: "))
english = int(input("enter your marks in english: "))
hindi = int(input("enter your marks in hindi: "))

total = maths + science + english + hindi

average = total/4

if science >= 35 and maths >= 35 and english >= 35 and hindi >= 32:
    print("pass")

else:
    print("fail")

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade obtained:", grade)

marks = {"maths": maths, "science": science, "english": english, "hindi": hindi}

highest_subject = max(marks, key=marks.get)
lowest_subject = min(marks, key=marks.get)

print("Highest subject:", highest_subject)
print("Lowest subject:", lowest_subject)

print("\n--- student performance report ---")
print("Name:", name)
print("Roll Number:", roll_number)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
print("Highest Subject:", highest_subject)
print("Lowest Subject:", lowest_subject)