import os

filename = input("Fayl yoki papka nomini kiriting: ")

if os.path.exists(filename):
    if os.path.isfile(filename):
        print(f"'{filename}' mavjud va bu FAYL.")
        print(f"Fayl hajmi: {os.path.getsize(filename)} bytes")
    elif os.path.isdir(filename):
        print(f"'{filename}' mavjud va bu PAPKA.")
else:
    print(f"Bunday fayl yoki papka mavjud emas.")
