import os

folder_name = input('Papka nomi: ').strip()
if os.path.exists(folder_name):
    print('Bu papka allaqachon mavjud.')
else:
    os.mkdir(folder_name)
    print(f'{folder_name} papkasi yaratildi.')
