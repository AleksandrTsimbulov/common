import sys

reader = sys.stdin
n = int(reader.readline())
list_A = [int(i) for i in reader.readline().split()]
INF = -(10 ** 10)
F = [INF] * (len(list_A) + 1)
F[0] = - INF
index_list = []
for i in range(len(list_A)):
    left = 0
    right = len(list_A)
    while right - left > 1:
        middle = (left + right) // 2
        if F[middle] < list_A[i]:
            right = middle
        else:
            left = middle
    F[right] = list_A[i]
    # print(right)
    # print(index_list)
    # print(F[right])
    if right > len(index_list):
        index_list.append([i])
    else:
        index_list[right - 1].append(i)
count1 = len(index_list)
ans = []
last_index = index_list.pop()[0]
ans.append(last_index + 1)
while index_list:
    for item in index_list.pop():
        if list_A[last_index] <= list_A[item]:
            last_index = item
            ans.append(last_index + 1)
            break
ans.reverse()
print(count1)
print(" ".join(str(i) for i in ans))
# 10
# 7 6 1 6 4 1 2 4 10 1