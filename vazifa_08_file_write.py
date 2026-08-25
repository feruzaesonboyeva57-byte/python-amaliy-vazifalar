students = ['Ali\n', 'Vali\n', 'Sardor\n', 'Madina\n', 'Aziza\n']
with open('students.txt', 'w', encoding='utf-8') as file:
    file.writelines(students)
print('Ma\'lumotlar yozildi.')
