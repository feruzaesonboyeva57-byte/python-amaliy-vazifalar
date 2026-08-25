import os, glob

print("--- AMALIY 1 & 2: Linux fayllar bilan ishlash ---")
files = [f for f in os.listdir('python_practice') if os.path.isfile(os.path.join('python_practice', f))]

py_files = [f for f in files if f.endswith('.py')]
txt_files = [f for f in files if f.endswith('.txt')]

print(".py fayllar:", py_files)
print(".txt fayllar:", txt_files)
print("Jami fayllar soni:", len(files))
