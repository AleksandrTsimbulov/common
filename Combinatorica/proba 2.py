n = int(input())


numbers = [int(i) for i in range(n)]


updated_set = set(numbers)
print(updated_set)
updated_set.add(4)
print(updated_set)