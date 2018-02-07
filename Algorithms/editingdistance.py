# Editing distance
# Illustrates editing distance iterating algorithm
import sys

reader = sys.stdin
first_line = reader.readline().strip()
second_line = reader.readline().strip()
n = len(first_line)
m = len(second_line)
# print(n, m)
INF = 10**4
D = [[INF] * (n+1) for j in range(m+1)]
for i in range(n+1):
    D[0][i] = i
for j in range(m+1):
    D[j][0] = j
for j in range(1, m+1):
    for i in range(1, n+1):
        if first_line[i-1] == second_line[j-1]: #corresponding letters match/not match
            c = 0
        else:
            c = 1
        D[j][i] = min([D[j-1][i] + 1, D[j][i-1] + 1, D[j-1][i-1] + c]) #ins, sub, match/diff
# print(D)
print(D[m][n])
# insert
# delete
# match/difference