list1 = [1, 2, 3]
list2 = [3, 5, 6]
count = sum([1 for num in list1 if num in list2])
print(count)