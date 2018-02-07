# Continuous rucksack
# Realization of one of greedy alrorithms
import sys

input = sys.stdin
n, W = map(int, input.readline().split())
item_list = []
for i in range(1, n+1):
    c, w = map(int, input.readline().split())
    volume_cost = c / w
    item_list.append([c, w, volume_cost])

def getkey(item):
    return item[2]

item_list.sort(key=getkey)
print(item_list)
total_cost = 0
while W:
    if item_list:
        cost, volume, volume_cost = item_list.pop()
        # print(cost, volume, volume_cost)
        if W >= volume:
            W -= volume
            total_cost += cost
        else:

            adder = W * volume_cost
            total_cost += adder
            break
    else:
        break
print('{0:.4f}'.format(total_cost))