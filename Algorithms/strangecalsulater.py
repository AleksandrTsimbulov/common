# The calculator
# Illustrates dinamic algorithm
import sys

x = int(input())
n_list = [i for i in range(x+1)]
D_list = [-1 for i in range(x+1)]
INF = 10**6

def check2(number):
    if number % 2 == 0:
        return D_list[(number // 2)] + 1
    else:
        return INF

def check3(number):
    if number % 3 == 0:
        return D_list[(number // 3)] + 1
    else:
        return INF

def fillD_list():
    for i in range(1, x+1):
        if D_list[i] == -1:
            D_list[i] = min(D_list[i-1] + 1, check2(n_list[i]), check3(n_list[i]))
    return D_list[x]

def find_numbers(index, min_operations_old):
    if index == 0:
        return
    min_operations_upd = min_operations_old - 1
    possible1 = D_list[index -1]
    possible2 = n_list[index] % 2
    possible_3 = n_list[index] % 3
    if possible1 == min_operations_upd:
        ans_list.append(n_list[index-1])
        find_numbers(index - 1, min_operations_upd)
    elif possible2 == 0 and D_list[n_list[index]//2] == min_operations_upd:
        ans_list.append(n_list[index//2])
        find_numbers(index//2, min_operations_upd)
    elif possible_3 == 0 and D_list[n_list[index]//3] == min_operations_upd:
        ans_list.append(n_list[index//3])
        find_numbers(index//3, min_operations_upd)

D_list[1] = 0
min_operations = fillD_list()
print(min_operations)
# print(D_list)
ans_list = []
ans_list.append(x)
find_numbers(x, min_operations)
ans_list.reverse()
for item in ans_list[1:]:
    print(item, end=' ')
