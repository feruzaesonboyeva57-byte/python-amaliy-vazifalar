import os

file_name = input('Fayl nomi: ').strip()
if os.path.isfile(file_name):
    print(f'{file_name} mavjud.')
else:
    print(f'{file_name} mavjud emas.')
