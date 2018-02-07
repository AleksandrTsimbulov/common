# Ladder
# Illustrates dinamic algorithm
import sys

reader = sys.stdin
n = int(reader.readline().strip())
steps = list(map(int, reader.readline().strip().split()))
# print(n, steps)
INF = 10**7
sum_list = [INF for i in range(n+1)]
def max_sumUB(n, steps):
    if sum_list[n-1] == INF:
        if len(steps) == 1:
            sum = steps[0]
        elif len(steps) == 2:
            sum = max(steps[1], steps[1] + steps[0])
        else:
            sum = steps[-1] + max(max_sumUB(n-1, steps[:-1]), max_sumUB(n-2, steps[:-2]))
    else:
        return sum_list[n-1]
    sum_list[n-1] = sum
    return sum

print(max_sumUB(n, steps))