import sys

reader = sys.stdin
n = int(reader.readline())
list_A = [int(i) for i in reader.readline().split()]
list_D = [0] * n
for i in range(1, n+1):
    list_D[i-1] = 1
    for j in range(i-1):
        if list_A[i-1] % list_A[j] == 0 and list_D[j] + 1 > list_D[i-1]:
            list_D[i-1] = list_D[j] + 1
# print(list_A)
# print(list_D)
print(max(list_D))
