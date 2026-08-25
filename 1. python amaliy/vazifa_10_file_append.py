new_student = input('Yangi student: ').strip()
with open('students.txt', 'a', encoding='utf-8') as file:
    file.write(f'\n{new_student}')
print('Qo\'shildi.')
