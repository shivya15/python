numbers =[5,2,2,1,7,7,4,4,4,2,3,2,4,4]
unique =[]
for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)