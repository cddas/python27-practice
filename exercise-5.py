import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a_new = list(set(a))
b_new = list(set(b))

def new_list_with_common_entry(a_new, b_new):
    c = []
    for item_a in a_new:
        for item_b in b_new:
            if (item_a == item_b):
                c.append(item_a)
    print(c)

#solution to 5-a
new_list_with_common_entry(a_new, b_new)

#solution to 5-b
list_a , list_b = [],[]
for val_a in range(16):
    list_a.append(random.randint(1,250))
print(list_a)

for val_b in range(26):
    list_b.append(random.randint(1,200))
print(list_b)

new_list_with_common_entry(list_a, list_b)

#solution to 5-c
print([item_a for item_a in a_new for item_b in b_new if (item_a == item_b)])