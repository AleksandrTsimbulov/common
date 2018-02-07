# Parallel processing
# Calculates what processor from n will handle tasks n from A with duration A[i] and stdout processor id and time it starts
import sys

input_data = sys.stdin
n, m = tuple(map(int, input_data.readline().strip().split()))
A = [int(i) for i in input_data.readline().strip().split()]
A.reverse()

def shdown_min(element_index):
    # shifts down the element in binary tree to its correct position in the heap
    minindex = element_index
    last_index = len(pr_heap) - 1
    leftchild_index = 2*element_index + 1
    if leftchild_index <= last_index and pr_heap[minindex][0] >= pr_heap[leftchild_index][0]:
        if pr_heap[minindex][0] > pr_heap[leftchild_index][0]:
            minindex = leftchild_index
        elif pr_heap[minindex][1] > pr_heap[leftchild_index][1]:
            minindex = leftchild_index
    rightchild_index = 2*element_index + 2
    if rightchild_index <= last_index and pr_heap[minindex][0] >= pr_heap[rightchild_index][0]:
        if pr_heap[minindex][0] > pr_heap[rightchild_index][0]:
            minindex = rightchild_index
        elif pr_heap[minindex][1] > pr_heap[rightchild_index][1]:
            minindex = rightchild_index
    if element_index != minindex:
        pr_heap[element_index], pr_heap[minindex] = pr_heap[minindex], pr_heap[element_index]
        shdown_min(minindex)  # recursion stops when there are no elements down smaller than current


def shup_min(element_index):
    # shifts up the element in binary tree to its correct position in the heap
    while element_index > 0 and pr_heap[element_index][0] <= pr_heap[(element_index-1)//2][0]:  # until the element is not in the root
        # print(element_index, current_element)
        if pr_heap[element_index][0] < pr_heap[(element_index-1)//2][0]:
            pr_heap[(element_index - 1) // 2], pr_heap[element_index] = pr_heap[element_index], pr_heap[(element_index-1)//2]
            element_index = (element_index-1)//2
        elif pr_heap[element_index][1] < pr_heap[(element_index-1)//2][1]:
            pr_heap[(element_index - 1) // 2], pr_heap[element_index] = pr_heap[element_index], pr_heap[(element_index-1)//2]
            element_index = (element_index - 1) // 2
        else:
            break


def get_min():
    # returns minimum of the heap time, doesn't change the heap itself
    return pr_heap[0][0]


def extract_min():
    # extracts min from the mean heap and remove it
    pr_heap[0], pr_heap[-1] = pr_heap[-1], pr_heap[0]
    result = pr_heap.pop()
    shdown_min(0)
    return result


def decreas_remaining_time(timer_jump):
    # changes all priorities by decreasing them by 1
    for item in pr_heap:
        item[0] -= timer_jump


def insert(element, pr_number, duration):
    # inserts element in the heap and placed it to correct position with its process number
    pr_heap.append([element, pr_number, duration])
    last_index = len(pr_heap) - 1
    shup_min(last_index)


def first_proc():
    tasks_exist = True
    while A:
        for i in range(n):
            if A:  # len(A) is more than n
                duration = A.pop()
                insert(duration + start_time, i, duration)
                ans_list.append((i, start_time))
            else:
                tasks_exist = False
                break  # A is less than 'n'
        break
    return tasks_exist

ans_list = []
pr_heap = []
start_time = 0
# main part
tasks_exist = first_proc()
while A and tasks_exist:
    freed_proc = extract_min()
    start_time = freed_proc[0]
    duration = A.pop()
    ans_list.append((freed_proc[1], start_time))
    insert(duration + start_time, freed_proc[1], duration)


for item in ans_list:
    print(item[0], item[1])