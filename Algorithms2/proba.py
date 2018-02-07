# Set with summation on segment implementation
# Illustrates realization of binary search tree in usage
import sys


def add_value(additional_value):
    # adds now value in searching tree
    root_index = search_tree[0][1]

    def search_and_add(additional_value, vertex_index):
        # recursion search of value into tree and if no, add it
        key = search_tree[vertex_index][0]
        right_ch = search_tree[vertex_index][2]
        left_ch = search_tree[vertex_index][1]
        if additional_value == key:  # if there is an element, do nothing
            return
        elif additional_value > key:
            if right_ch != -1:  # if there is a right child, go on searching
                search_and_add(additional_value, right_ch)
            else:  # if there is no right child, add element as a right child
                new_record = tree_record(additional_value, -1, -1, vertex_index, False)
                new_record_index = len(search_tree)
                search_tree[vertex_index][2] = new_record_index
                search_tree.append(new_record)
                return
        elif additional_value < key:
            if left_ch != -1:  # if there is a left child, go on searching
                search_and_add(additional_value, left_ch)
            else:  # if there is no left child, add element as a left child
                new_record = tree_record(additional_value, -1, -1, vertex_index, True)
                new_record_index = len(search_tree)
                search_tree[vertex_index][1] = new_record_index
                search_tree.append(new_record)
                return
    if len(search_tree) == 1:
        new_record = tree_record(additional_value, -1, -1, root_index, False)
        new_record_index = len(search_tree)
        search_tree[root_index][1] = new_record_index
        search_tree.append(new_record)
        return
    else:
        search_and_add(additional_value, root_index)
    return


def search_value(searching_value):
    # search value in searching tree and prints result
    root_index = search_tree[0][1]

    def search(searching_value, root_index):
        # recursion search of value into tree
        key = search_tree[root_index][0]
        right_ch = search_tree[root_index][2]
        left_ch = search_tree[root_index][1]
        if searching_value == key:
            print('Found')
            return
        elif searching_value > key:
            if right_ch != -1:  # if there is a right child, go on searching
                search(searching_value, right_ch)
            else:  # when no more right child, stop and print result
                print('Not found')
                return
        elif searching_value < key:
            if left_ch != 1:  # if there is a left child, go on searching
                search(searching_value, left_ch)
            else:  # when no more left child, stop and print result
                print('Not found')
                return
    search(searching_value, root_index)



def delete_value(delete_request):
    pass


def sum_value(sum_request):
    global prev_sum
    pass


def f_function(value):
    global prev_sum
    resulted_f = (value + prev_sum) % 1000000001
    return resulted_f


def tree_record(key, left, right, parent, is_left):
    return [key, left, right, parent, is_left]


# getting request
requests = sys.stdin
n = int(requests.readline().strip())
list_of_request = []
for i in range(n):
    list_of_request.append(list(requests.readline().strip().split()))
list_of_request.reverse()
# set constants and global variables
prev_sum = 0
# set binary search tree
search_tree = [['root', 0]]
# main program
while list_of_request:
    request = list_of_request.pop()
    if request[0] == '+':
        additional_value = int(request[1])
        add_value(additional_value)
    elif request[0] == '-':
        delete_value(request)
    elif request[0] == '?':
        if len(search_tree) == 1:
            print('Not found')
            continue
        else:
            additional_value = int(request[1])
            search_value(additional_value)
    elif request[0] == "s":
        sum_value(request)
    else:
        print('wrong input data format')
print(search_tree)
