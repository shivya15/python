from pathlib import Path

path=Path("Basics")
print(path.exists())

path4=Path("Oops")
print(path.exists())

path1=Path("emails")
print(path1.exists())
#path1.rmdir()

path2=Path()
files=path.glob('*.py')

for file in files:
    print(file)

