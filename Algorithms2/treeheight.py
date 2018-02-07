# Tree height
# Illustrates recursive method for tree height calculation
import sys

input_d = sys.stdin
n = int(input_d.readline())
tree_list = tuple(map(int, input_d.readline().split()))
root_index = tree_list.index(-1)
tree_dict = {i:[] for i in range(n)}
for index, item in enumerate(tree_list):
    if item != -1:
        tree_dict[item].append(index)
sys.setrecursionlimit(50000)

def height(root_index):
    #culculates height of the tree recursivly
    ht = 1
    for child in tree_dict[root_index]:
        ht = max(ht, 1 + height(child))
    return ht

height_tree = height(root_index)
print(height_tree)