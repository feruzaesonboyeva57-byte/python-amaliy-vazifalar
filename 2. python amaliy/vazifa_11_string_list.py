data = """Ali Valiyev
Madina Karimova
Bekzod Toshmatov
Aziza Qodirova
Jasur Abdullayev"""

with open("students_full.txt", "w") as f:
    f.write(data)

names = []
surnames = []

with open("students_full.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split()
            names.append(parts[0])
            surnames.append(parts[1])

print("Names:", names)
print("Surnames:", surnames)

a_names = [name for name in names if name.startswith("A")]
print("'A' bilan boshlanadigan ismlar:", a_names)
