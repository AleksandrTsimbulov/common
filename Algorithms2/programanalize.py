# Program analize
# Prints 1 if there are possible variables and 0 if there aren't

import sys

input_data = sys.stdin
reader = (map(int, line.strip().split()) for line in input_data)
n, e, d = tuple(next(reader))
rank = [-1] + [0*i for i in range(n)]
parent = [-1] + list(range(1, n+1))


def find(element):
    # finds id (root) of the set of the element and shrinks the path
    if element != parent[element]:
        parent[element] = find(parent[element])
    return parent[element]


def union(i, j):
    # collides two sets into one and calc max line numbers(rank)
    i_id = find(i)
    j_id = find(j)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
    else:
        parent[i_id] = j_id
        if rank[i_id] == rank[j_id]:
            rank[j_id] += 1


# receiving requests and unites the tables
for number in range(e):
    union(*tuple(next(reader)))
for counter in range(d):
    i, j = tuple(next(reader))
    if find(i) == find(j):
        print(0)
        sys.exit()
print(1)
