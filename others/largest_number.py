largest_so_far = None

print("Before:", largest_so_far)
for i in [3, 5, 12, 74, 31, 9]:
    if largest_so_far is None or i > largest_so_far:
        largest_so_far = i 

print("After:", largest_so_far)
