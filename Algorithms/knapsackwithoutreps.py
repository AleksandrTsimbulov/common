# Knapsack without reps
# Illustrates algorithm of filling knapsack
import sys

reader = sys.stdin
W, n = tuple(map(int, reader.readline().strip().split()))
weights = [int(i) for i in reader.readline().strip().split()]
D = [[0 for j in range(W+1)] for i in range(n+1)]
for i in range(1, n+1):
    for w in range(1, W+1):
        D[i][w] = D[i-1][w]
        if weights[i-1] <= w:
            D[i][w] = max([D[i][w], D[i-1][w-weights[i-1]] + weights[i-1]])
print(D[n][W])