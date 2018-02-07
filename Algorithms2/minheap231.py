# Miminum heap
# Creates the heap from massive on place and provides necessary operations for the heap behaviour
import sys

input_data = sys.stdin
n = int(input_data.readline().strip())
A = [int(i) for i in input_data.readline().strip().split()]
ans_list = []

def shdown_min(element_index):
    # shifts down the element in binary tree to its correct position in the heap
    minindex = element_index
    last_index = len(A) - 1
    leftchild_index = 2*element_index + 1
    if leftchild_index <= last_index and A[minindex] > A[leftchild_index]:
        minindex = leftchild_index
    rightchild_index = 2*element_index + 2
    if rightchild_index <= last_index and A[minindex] > A[rightchild_index]:
        minindex = rightchild_index
    if element_index != minindex:
        A[element_index], A[minindex] = A[minindex], A[element_index]
        ans_list.append((element_index, minindex))
        shdown_min(minindex)  # recursion stops when there are no elements down smaller than current


def shup_min(element_index):
    # shifts up the element in binary tree to its correct position in the heap
    parent_element = A[(element_index-1)//2]
    current_element = A[element_index]
    while element_index > 0 and current_element < parent_element:  # until the element is not in the root
        parent_element, current_element = current_element, parent_element
        element_index = (element_index-1)//2
        # parent_element = A[(element_index - 1) // 2]
        # current_element = A[element_index]


def get_min():
    # returns minimum of the heap, doesn't change the heap itself
    return A[0]


def insert(element):
    # inserts element in the heap and placed it to correct position
    size = len(A) - 1
    size = size + 1
    A.append(element)
    shup_min(size)


def extract_min():
    # extracts min from the mean heap and remove it
    A[0], A[-1] = A[-1], A[0]
    result = A.pop()
    shdown_min(0)
    return result


def change_priority(element_index, new_priority):
    # changes priority of the element and changes its position
    old_priority = A[element_index]
    A[element_index] = new_priority
    if new_priority < old_priority:
        shup_min(element_index)
    else:
        shdown_min(element_index)


def remove(element_index):
    # removes the element from the min heap
    MINUS_INF = -10**21
    A[element_index] = MINUS_INF
    shup_min(element_index)
    extract_min()


def buildheap():
    last_index = len(A) - 1
    for i in range((last_index-1)//2, -1, -1):
        shdown_min(i)


buildheap()
print(len(ans_list))
for item in ans_list:
    print(item[0], item[1])