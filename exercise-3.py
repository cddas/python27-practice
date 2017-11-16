#Solution to exercise-3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

#solution exercise-3a,3b
for value in a:
    if (value > 5):
        print(value)
        b.append(value)
print(b)

#solution exercise-3c
print([value for value in a if (value > 5)])

#solution exercise-3d
new_num = raw_input("Enter a mumber to check : ")
print([value for value in a if (value > int(new_num))])



