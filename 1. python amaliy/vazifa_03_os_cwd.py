import os

print('Joriy papka:', os.getcwd())
print('Elementlar:')
for item in os.listdir():
    print('-', item)
