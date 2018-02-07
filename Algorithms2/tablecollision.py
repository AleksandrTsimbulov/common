# Table collision
# Collide tables and prints max table size after collision

import sys

input_data = sys.stdin
reader = (map(int, line.strip().split()) for line in input_data)
n, m = tuple(next(reader))
rank = [-1] + list(next(reader))
parent = [-1] + list(range(1, n+1))
current_max = max(rank)


def find(element):
    # finds id (root) of the set of the element and shrinks the path
    if element != parent[element]:
        parent[element] = find(parent[element])
    return parent[element]


def union(destination, source):
    # collides two sets into one and calc max line numbers(rank)
    global current_max
    destin_id = find(destination)
    source_id = find(source)
    if destin_id == source_id:
        return
    parent[source_id] = destin_id
    rank[destin_id] += rank[source_id]
    rank[source_id] = 0
    if current_max < rank[destin_id]:
        current_max = rank[destin_id]

# receiving requests and unites the tables
for j in range(m):
    union(*tuple(next(reader)))
    print(current_max)
