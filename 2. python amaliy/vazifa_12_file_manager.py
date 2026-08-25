import os, shutil

def file_manager():
    while True:
        print("\n===== FILE MANAGER =====")
        print("1. Papkadagi fayllarni ko'rish")
        print("2. Yangi papka yaratish")
        print("3. Yangi fayl yaratish")
        print("4. Faylni o'qish")
        print("5. Faylga yozish")
        print("6. Faylni o'chirish")
        print("7. Papkani o'chirish")
        print("8. Fayl hajmini ko'rish")
        print("9. Chiqish")
        
        choice = input("\nTanlang: ")
        
        if choice == '1':
            print("\nPapkadagi elementlar:")
            for item in os.listdir():
                print("-", item)
        elif choice == '2':
            name = input("Papka nomi: ")
            if not os.path.exists(name):
                os.mkdir(name)
                print("Papka yaratildi.")
            else:
                print("Mavjud papka!")
        elif choice == '3':
            name = input("Fayl nomi: ")
            open(name, 'w').close()
            print("Fayl yaratildi.")
        elif choice == '4':
            name = input("Fayl nomi: ")
            if os.path.isfile(name):
                with open(name, 'r') as f:
                    print("\nFayl mazmuni:\n" + f.read())
            else:
                print("Fayl topilmadi!")
        elif choice == '5':
            name = input("Fayl nomi: ")
            text = input("Yoziladigan matn: ")
            with open(name, 'a') as f:
                f.write(text + "\n")
            print("Matn yozildi.")
        elif choice == '6':
            name = input("O'chiriladigan fayl: ")
            if os.path.isfile(name):
                os.remove(name)
                print("Fayl o'chirildi.")
            else:
                print("Fayl topilmadi!")
        elif choice == '7':
            name = input("O'chiriladigan papka: ")
            if os.path.isdir(name):
                shutil.rmtree(name)
                print("Papka o'chirildi.")
            else:
                print("Papka topilmadi!")
        elif choice == '8':
            name = input("Fayl nomi: ")
            if os.path.isfile(name):
                print(f"Hajmi: {os.path.getsize(name)} bytes")
            else:
                print("Fayl topilmadi!")
        elif choice == '9':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    file_manager()
