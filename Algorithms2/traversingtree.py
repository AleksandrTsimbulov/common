# Traversing tree
# Illustrates an algorithm of traversing through binary tree
import sys

# getting binary tree
data = sys.stdin
binary_tee = []
n = int(data.readline().strip())
for i in range(n):
    binary_tee.append([int(x) for x in data.readline().strip().split()])
# in-order traversing

def in_order_travers(root):
    # in order traversing of the binary tree
    if binary_tee[root][1] != -1:
        in_order_travers(binary_tee[root][1])
    print(binary_tee[root][0], end=' ')
    if binary_tee[root][2] != -1:
        in_order_travers(binary_tee[root][2])


def pre_order_travers(root):
    # pre-order traversing of the binary tree
    print(binary_tee[root][0], end=' ')
    if binary_tee[root][1] != -1:
        pre_order_travers(binary_tee[root][1])
    if binary_tee[root][2] != -1:
        pre_order_travers(binary_tee[root][2])


def post_order_travers(root):
    # post-order traversing of the binary tree
    if binary_tee[root][1] != -1:
        post_order_travers(binary_tee[root][1])
    if binary_tee[root][2] != -1:
        post_order_travers(binary_tee[root][2])
    print(binary_tee[root][0], end=' ')


in_order_travers(0)
print()
pre_order_travers(0)
print()
post_order_travers(0)