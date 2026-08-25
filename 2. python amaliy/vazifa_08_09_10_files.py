import os

students = ["Ali", "Vali", "Sardor", "Madina", "Aziza"]
with open("students.txt", "w") as f:
    f.write("\n".join(students) + "\n")

print("--- Fayldan o'qish ---")
with open("students.txt", "r") as f:
    print("Talabalar:\n" + f.read())

new_student = "Shahnoza"
with open("students.txt", "a") as f:
    f.write(new_student + "\n")

print(f"--- '{new_student}' qo'shilgandan so'ng ---")
with open("students.txt", "r") as f:
    print(f.read())
