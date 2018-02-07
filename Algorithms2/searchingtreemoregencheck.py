# Searching tree check 2.0
# Illustrates searching tree check realisation
import sys


def is_correct_tree(root, minim, maxim):
    # checks if the binary tree is a correct searching tree
    global is_correct
    if not is_correct:
        return
    key = binary_tee[root][0]
    left_child = binary_tee[root][1]
    right_child = binary_tee[root][2]
    if key < minim or key >= maxim:
        is_correct = False
        return
    if left_child != -1:
        is_correct_tree(left_child, minim, key)
    if right_child != -1:
        is_correct_tree(right_child, key, maxim)


# getting binary tree
data = sys.stdin
binary_tee = []
n = int(data.readline().strip())
for i in range(n):
    binary_tee.append([int(x) for x in data.readline().strip().split()])
# set constants
CORRECT = 'CORRECT'
INCORRECT = 'INCORRECT'
MIN = -1 * (2**31) - 1
MAX = 2**31
sys.setrecursionlimit(1000000)
# search tree checking
if n == 0:
    print(CORRECT)
    sys.exit()
is_correct = True
is_correct_tree(0, MIN, MAX)
# print the result
if is_correct:
    print(CORRECT)
else:
    print(INCORRECT)
