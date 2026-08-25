names = ['ali', 'vali', 'sardor', 'madina', 'aziza']
upper_names = [name.upper() for name in names]
cap_names = [name.capitalize() for name in names]
names_with_a = [name for name in names if 'a' in name.lower()]
count_a = len(names_with_a)

print('Katta harfda:', upper_names)
print('Capitalize:', cap_names)
print('a qatnashganlar:', names_with_a)
print('a bor ismlar soni:', count_a)
