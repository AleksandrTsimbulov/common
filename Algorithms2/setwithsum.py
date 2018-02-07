# Set with summation on segment implementation
# Illustrates realization of binary search tree in usage
import sys


def add_value(additional_value):
    # adds now value in searching tree
    def search_and_add(additional_value, vertex_key):
        # recursion search of value into tree and if no, add it
        right_ch = search_tree[vertex_key][1]
        left_ch = search_tree[vertex_key][0]
        if additional_value == vertex_key:  # if there is an element, do nothing
            return
        elif additional_value > vertex_key:
            if right_ch != -1:  # if there is a right child, go on searching
                search_and_add(additional_value, right_ch)
            else:  # if there is no right child, add element as a right child
                new_record = tree_record(-1, -1, vertex_key, False, 1)
                search_tree[additional_value] = new_record
                search_tree[vertex_key][1] = additional_value
                balance_tree(vertex_key)
                return
        elif additional_value < vertex_key:
            if left_ch != -1:  # if there is a left child, go on searching
                search_and_add(additional_value, left_ch)
            else:  # if there is no left child, add element as a left child
                new_record = tree_record(-1, -1, vertex_key, True, 1)
                search_tree[additional_value] = new_record
                search_tree[vertex_key][0] = additional_value
                balance_tree(vertex_key)
                return
    if len(search_tree) == 1:
        search_tree['root'] = additional_value
        root_key = search_tree['root']
        new_record = tree_record(-1, -1, root_key, False, 1)
        search_tree[additional_value] = new_record
        return
    root_key = search_tree['root']
    search_and_add(additional_value, root_key)
    return


def search_value(searching_value):
    # search value in searching tree and prints result
    def search(searching_value, vertex_key):
        # recursion search of value into tree
        right_ch = search_tree[vertex_key][1]
        left_ch = search_tree[vertex_key][0]
        if searching_value == vertex_key:
            print('Found')
            return
        elif searching_value > vertex_key:
            if right_ch != -1:  # if there is a right child, go on searching
                search(searching_value, right_ch)
            else:  # when no more right child, stop and print result
                print('Not found')
                return
        elif searching_value < vertex_key:
            if left_ch != -1:  # if there is a left child, go on searching
                search(searching_value, left_ch)
            else:  # when no more left child, stop and print result
                print('Not found')
                return
    if len(search_tree) == 1:
        print('Not found')
        return
    root_key = search_tree['root']
    search(searching_value, root_key)
    return


def delete_value(removing_val):
    # delete vertex in searching tree
    def search_for_del(searching_value, vertex_key):
        # recursion search of value into tree and delete it
        def get_previous_element_key(key):
            right_ch = search_tree[key][1]
            if right_ch != -1:
                get_previous_element_key(right_ch)
            else:
                return key
        right_ch = search_tree[vertex_key][1]
        left_ch = search_tree[vertex_key][0]
        if searching_value == vertex_key:  # required vertex is found
            parent_key = search_tree[vertex_key][2]
            is_left = search_tree[vertex_key][3]
            if left_ch == -1 and right_ch == -1:  # vertex is a leaf
                if parent_key == vertex_key:  # vertex is the root
                    search_tree['root'] = 0
                    del search_tree[searching_value]
                    return
                if is_left:
                    search_tree[parent_key][0] = -1
                else:
                    search_tree[parent_key][1] = -1
                del search_tree[searching_value]
                balance_tree(parent_key)
                return
            elif left_ch == -1 or right_ch == -1:  # vertex has only one child
                if parent_key == vertex_key:  # vertex is the root
                    if left_ch != -1:
                        search_tree['root'] = left_ch
                        search_tree[left_ch][2] = left_ch
                        del search_tree[searching_value]
                        return
                    else:
                        search_tree['root'] = right_ch
                        search_tree[right_ch][2] = right_ch
                        del search_tree[searching_val]
                        return
                if is_left:
                    if left_ch != -1:
                        search_tree[parent_key][0] = left_ch
                    else:
                        search_tree[parent_key][0] = right_ch
                else:
                    if left_ch != -1:
                        search_tree[parent_key][1] = left_ch
                    else:
                        search_tree[parent_key][1] = right_ch
                del search_tree[searching_value]
                balance_tree(parent_key)
                return
            else:  # vertex has two children
                left_key = search_tree[vertex_key][0]
                prev_el_key = get_previous_element_key(left_key)
                parent_prev_el = search_tree[prev_el_key][2]
                if parent_prev_el == searching_val:
                    search_tree[prev_el_key][1] = search_tree[searching_val][1]
                    search_tree[prev_el_key][3] = search_tree[searching_val][3]
                    if search_tree[searching_val][2] != searching_val:
                        search_tree[prev_el_key][2] = search_tree[searching_val][2]
                        if search_tree[searching_val][3] == True:
                            search_tree[search_tree[searching_val][2]][0] = prev_el_key
                        else:
                            search_tree[search_tree[searching_val][2]][1] = prev_el_key
                    else:
                        search_tree[prev_el_key][2] = prev_el_key
                        search_tree['root'] = prev_el_key
                    del search_tree[searching_value]
                    balance_tree(prev_el_key)
                    return
                else:
                    key_for_balance = parent_prev_el
                    search_tree[parent_prev_el][1] = search_tree[prev_el_key][0]
                    if search_tree[prev_el_key][0] != -1:
                        search_tree[search_tree[prev_el_key][0]][2] = parent_prev_el
                        search_tree[search_tree[prev_el_key][0]][3] = False
                    search_tree[prev_el_key][0] = search_tree[searching_val][0]
                    search_tree[prev_el_key][1] = search_tree[searching_val][1]
                    search_tree[prev_el_key][3] = search_tree[searching_val][3]
                    if search_tree[searching_val] != searching_val:
                        search_tree[prev_el_key][2] = search_tree[searching_val][2]
                        if search_tree[searching_val][3] == True:
                            search_tree[search_tree[searching_val][2]][0] = prev_el_key
                        else:
                            search_tree[search_tree[searching_val][2]][1] = prev_el_key
                    else:
                        search_tree[prev_el_key][2] = prev_el_key
                        search_tree['root'] = prev_el_key
                    del search_tree[searching_value]
                    balance_tree(key_for_balance)
                    return
        elif searching_value > vertex_key:
            if right_ch != -1:  # if there is a right child, go on searching
                search_for_del(searching_value, right_ch)
            else:  # when no more right child, stop and do nothing
                return
        elif searching_value < vertex_key:
            if left_ch != -1:  # if there is a left child, go on searching
                search_for_del(searching_value, left_ch)
            else:  # when no more left child, stop and do nothing
                return
    if len(search_tree) == 1:
        return
    root_key = search_tree['root']
    search_for_del(removing_val, root_key)
    return


def sum_value(sum_request):
    global prev_sum
    pass


def f_function(value):
    global prev_sum
    resulted_f = (value + prev_sum) % 1000000001
    print('result from f_function: ', value, prev_sum, resulted_f)
    return resulted_f


def tree_record(left, right, parent, is_left, tree_height):
    # creates a record for a new vertex
    return [left, right, parent, is_left, tree_height]


def balance_tree(new_vertex_key):
    # balancing AVL tree
    print('balancing')
    def height_calc(vert_key):
        if search_tree[vert_key][0] != -1:
            left_height = search_tree[search_tree[vert_key][0]][4]
        else:
            left_height = 0
        if search_tree[vert_key][1] != -1:
            right_height = search_tree[search_tree[vert_key][1]][4]
        else:
            right_height = 0
        search_tree[vert_key][4] = max(left_height, right_height) + 1
        return
    # recalculate current height based on children heights
    if search_tree[new_vertex_key][0] != -1:
        left_height = search_tree[search_tree[new_vertex_key][0]][4]
    else:
        left_height = 0
    if search_tree[new_vertex_key][1] != -1:
        right_height = search_tree[search_tree[new_vertex_key][1]][4]
    else:
        right_height = 0
    search_tree[new_vertex_key][4] = max(left_height, right_height) + 1
    # parent_key = search_tree[new_vertex_key][2]
    # if parent_key == new_vertex_key:  # if root than no balancing is required
    #     return
    # check if balance is required
    alfa_vertex_key = new_vertex_key
    if abs(left_height - right_height) > 1:
        if right_height > left_height:  # right rotation
            beta_vertex_key = search_tree[alfa_vertex_key][1]
            if search_tree[beta_vertex_key][1] >= search_tree[beta_vertex_key][0]:  # small right rotation
                search_tree[alfa_vertex_key][1] = search_tree[beta_vertex_key][0]
                search_tree[beta_vertex_key][0] = alfa_vertex_key
                temp_alf_par = search_tree[alfa_vertex_key][2]
                if temp_alf_par == alfa_vertex_key:
                    it_was_root = True
                temp_isleft = search_tree[alfa_vertex_key][3]
                search_tree[alfa_vertex_key][2] = beta_vertex_key
                if it_was_root:
                    search_tree[beta_vertex_key][2] = beta_vertex_key
                    search_tree['root'] = beta_vertex_key
                else:
                    search_tree[beta_vertex_key][2] = temp_alf_par
                search_tree[beta_vertex_key][3] = temp_isleft
                search_tree[alfa_vertex_key][3] = True
                if search_tree[alfa_vertex_key][1] != -1:
                    search_tree[search_tree[alfa_vertex_key][1]][3] = False
                height_calc(alfa_vertex_key)
                height_calc(beta_vertex_key)
                highest_vert = beta_vertex_key
            else:  # big right rotation
                gamma_key = search_tree[beta_vertex_key][0]
                search_tree[alfa_vertex_key][1] = search_tree[gamma_key][0]
                if search_tree[alfa_vertex_key][1] != -1:
                    search_tree[search_tree[alfa_vertex_key][1]][3] = False
                    search_tree[search_tree[alfa_vertex_key][1]][2] = alfa_vertex_key
                search_tree[beta_vertex_key][0] = search_tree[gamma_key][1]
                if search_tree[beta_vertex_key][0] != -1:
                    search_tree[search_tree[beta_vertex_key][0]][3] = True
                    search_tree[search_tree[beta_vertex_key][0]][2] = beta_vertex_key
                temp_isleft = search_tree[alfa_vertex_key][3]
                temp_alf_par = search_tree[alfa_vertex_key][2]
                if temp_alf_par == alfa_vertex_key:
                    it_was_root = True
                search_tree[alfa_vertex_key][2] = gamma_key
                search_tree[alfa_vertex_key][3] = True
                search_tree[beta_vertex_key][2] = gamma_key
                search_tree[beta_vertex_key][3] = False
                if it_was_root:
                    search_tree[gamma_key][2] = gamma_key
                    search_tree['root'] = gamma_key
                else:
                    search_tree[gamma_key][2] = temp_alf_par
                search_tree[gamma_key][3] = temp_isleft
                height_calc(alfa_vertex_key)
                height_calc(beta_vertex_key)
                height_calc(gamma_key)
                highest_vert = gamma_key
        else:  # left rotation
            beta_vertex_key = search_tree[alfa_vertex_key][0]
            if search_tree[beta_vertex_key][0] >= search_tree[beta_vertex_key][1]:  # small left rotation
                search_tree[alfa_vertex_key][0] = search_tree[beta_vertex_key][1]
                search_tree[beta_vertex_key][1] = alfa_vertex_key
                temp_alf_par = search_tree[alfa_vertex_key][2]
                if temp_alf_par == alfa_vertex_key:
                    it_was_root = True
                temp_isleft = search_tree[alfa_vertex_key][3]
                search_tree[alfa_vertex_key][2] = beta_vertex_key
                search_tree[alfa_vertex_key][3] = False
                if it_was_root:
                    search_tree[beta_vertex_key][2] = beta_vertex_key
                    search_tree['root'] = beta_vertex_key
                else:
                    search_tree[beta_vertex_key][2] = temp_alf_par
                search_tree[beta_vertex_key][3] = temp_isleft
                if search_tree[alfa_vertex_key][0] != -1:
                    search_tree[search_tree[alfa_vertex_key][0]][3] = True
                height_calc(alfa_vertex_key)
                height_calc(beta_vertex_key)
                highest_vert = beta_vertex_key
            else:  # big left rotation
                gamma_key = search_tree[beta_vertex_key][1]
                search_tree[alfa_vertex_key][0] = search_tree[gamma_key][1]
                if search_tree[alfa_vertex_key][0] != -1:
                    search_tree[search_tree[alfa_vertex_key][0]][3] = True
                    search_tree[search_tree[alfa_vertex_key][0]][2] = alfa_vertex_key
                search_tree[beta_vertex_key][1] = search_tree[gamma_key][0]
                if search_tree[beta_vertex_key][1] != -1:
                    search_tree[search_tree[beta_vertex_key][1]][2] = beta_vertex_key
                    search_tree[search_tree[beta_vertex_key][1]][3] = False
                temp_isleft = search_tree[alfa_vertex_key][3]
                temp_alf_par = search_tree[alfa_vertex_key][2]
                if temp_alf_par == alfa_vertex_key:
                    it_was_root = True
                search_tree[alfa_vertex_key][2] = gamma_key
                search_tree[alfa_vertex_key][3] = False
                search_tree[beta_vertex_key][2] = gamma_key
                search_tree[beta_vertex_key][3] = True
                if it_was_root:
                    search_tree[gamma_key][2] = gamma_key
                    search_tree['root'] = gamma_key
                else:
                    search_tree[gamma_key][2] = temp_alf_par
                search_tree[gamma_key][3] = temp_isleft
                height_calc(alfa_vertex_key)
                height_calc(beta_vertex_key)
                height_calc(gamma_key)
                highest_vert = gamma_key
        if highest_vert != search_tree[highest_vert][2]:
            balance_tree(search_tree[highest_vert][2])
        else:
            return
    else:
        highest_vert = new_vertex_key
        if highest_vert != search_tree[highest_vert][2]:
            balance_tree(search_tree[highest_vert][2])
        else:
            return


# getting request
requests = sys.stdin
n = int(requests.readline().strip())
list_of_request = []
for i in range(n):
    list_of_request.append(list(requests.readline().strip().split()))
list_of_request.reverse()
# set constants and global variables
prev_sum = 3
# set binary search tree
search_tree = {'root': 0}
# main program
while list_of_request:
    request = list_of_request.pop()
    if request[0] == '+':
        additional_value = f_function(int(request[1]))
        add_value(additional_value)
        print(search_tree)
    elif request[0] == '-':
        removing_val = f_function(int(request[1]))
        delete_value(removing_val)
        print(search_tree)
    elif request[0] == '?':
        searching_val = f_function(int(request[1]))
        search_value(searching_val)
        print(search_tree)
    elif request[0] == "s":
        sum_value(request)
        print(search_tree)
    else:
        print('wrong input data format')
print(search_tree)
