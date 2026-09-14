# 1. str
text_val = "Hello Python"

# 2. int
int_val = 25

# 3. float
float_val = 3.14

# 4. bool
bool_val = True

# 5. list
list_val = ["apple", "banana", "cherry"]

# 6. tuple
tuple_val = (10, 20, 30)

# 7. set
set_val = {1, 2, 3, 4}

# 8. dict
dict_val = {"name": "Ali", "age": 20}

# Barcha o'zgaruvchilarni ro'yxatga olamiz
data_types = [
    text_val,
    int_val,
    float_val,
    bool_val,
    list_val,
    tuple_val,
    set_val,
    dict_val,
]

# 9-10. Qiymatlarni va ularning type() natijasini chiqarish
print("=== Python Data Types va Ularning Turlari ===")
for data in data_types:
    print(f"Qiymat: {data} | Turi: {type(data)}")

print("\n" + "=" * 45 + "\n")

# 11. list, tuple, set va dict ustida for siklidan foydalanish
print("--- 1. List bo'ylab for sikli ---")
for item in list_val:
    print(f"List elementi: {item}")

print("\n--- 2. Tuple bo'ylab for sikli ---")
for item in tuple_val:
    print(f"Tuple elementi: {item}")

print("\n--- 3. Set bo'ylab for sikli ---")
for item in set_val:
    print(f"Set elementi: {item}")

print("\n--- 4. Dict bo'ylab for sikli ---")
for key, value in dict_val.items():
    print(f"Kalit: {key} -> Qiymat: {value}")
