array = input("Please enter array: ").split()
new_array = []

for i in array:
    if len(i) <= 3:
        new_array.append(i)

print(new_array)
