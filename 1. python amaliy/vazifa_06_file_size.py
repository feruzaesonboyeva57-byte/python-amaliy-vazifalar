import os

file_name = 'data.txt'
if os.path.exists(file_name):
    print(f'Fayl hajmi: {os.path.getsize(file_name)} bytes')
else:
    print(f'{file_name} topilmadi.')
