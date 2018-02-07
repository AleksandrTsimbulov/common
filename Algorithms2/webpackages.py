# Webpackages
# Illustrates FIFO stracture in algorithms
import sys

reader = sys.stdin
SIZE, n = tuple(map(int, reader.readline().split()))
if n == 0:
    sys.exit()
incoming_list = []
for i in range(n):
    incoming_list.append(tuple(map(int, reader.readline().split())) + (i,))
queue = [0 for k in range(SIZE)]
answer_list = [-1 for j in range(n)]

first_index = 0
free_space = SIZE
incoming_list.reverse()
current_time = 0
packages_at_a_time = 0
inc_time = 0

def buffer():
    buff = []
    if len(incoming_list) > 1 and (incoming_list[-1][0] == incoming_list[-2][0]):
        while len(incoming_list) > 1 and (incoming_list[-1][0] == incoming_list[-2][0]):
            buff.append(incoming_list.pop())
            buff.append(incoming_list.pop())
            if incoming_list and (buff[-1][0] == incoming_list[-1][0]):
                continue
            else:
                break
    if incoming_list and buff:
        if incoming_list[-1][0] == buff[-1][0]:
            buff.append(incoming_list.pop())
    if not buff:
        buff.append(incoming_list.pop())
    buff.reverse()
    return buff

def zero_dur_data(buff):
    global current_time
    if free_space == SIZE and buff[-1][1] == 0:
        if current_time <= buff[-1][0]:
            current_time = buff[-1][0]
            while buff and (buff[-1][1] == 0):
                index = buff.pop()[2]
                answer_list[index] = current_time

def put_on_stack(current_time, buff, free_space, SIZE, first_index=0):
    get_new_buff = False
    global packages_at_a_time
    if free_space > 0:
        if buff[-1][0] < current_time: # эмулируем заполнение тех слотов, которые были свободны во время работы процессора
            if free_space - packages_at_a_time > 0: # единственный случай наличия свободных слотов во время работы процессора
                if free_space - packages_at_a_time >= len(buff):
                    while buff:
                        insert_index = (first_index + (SIZE - free_space)) % SIZE
                        queue[insert_index] = buff.pop()
                        free_space -= 1
                    if free_space - packages_at_a_time > 0:
                        get_new_buff = True
                else:
                    while free_space - packages_at_a_time > 0:
                        insert_index = (first_index + (SIZE - free_space)) % SIZE
                        queue[insert_index] = buff.pop()
                        free_space -= 1
        elif buff[-1][0] == current_time:  # эмулируем заполнение всех свободных слотов ровно в момент прихода пакета (время совпадает с окончанием работы процессора)
            while free_space > 0 and buff:
                insert_index = (first_index + (SIZE - free_space)) % SIZE
                queue[insert_index] = buff.pop()
                free_space -= 1
    return free_space, get_new_buff


def process_it(first_index, free_space, SIZE):
    global current_time
    packages_at_a_time = 0
    if queue[first_index] != 0:
        package = queue[first_index]
        package_namber = package[2]
        answer_list[package_namber] = current_time
        current_time = current_time + package[1]
        queue[first_index] = 0
        first_index = (first_index + 1) % SIZE
        free_space += 1
        packages_at_a_time += 1
        while package[1] == 0: # if there are several packages on stack with '0' duration they must be processed sumaltaniously
            if queue[first_index] != 0:
                package = queue[first_index]
                package_namber = package[2]
                answer_list[package_namber] = current_time
                current_time = current_time + package[1]
                queue[first_index] = 0
                first_index = (first_index + 1) % SIZE
                free_space += 1
                packages_at_a_time += 1
            else:
                if incoming_list and current_time < incoming_list[-1][0]:
                    current_time = incoming_list[-1][0]
                break
    else:
        if incoming_list and current_time < incoming_list[-1][0]:
            current_time = incoming_list[-1][0]
    return first_index, free_space, packages_at_a_time

while True:
    if incoming_list:
        if incoming_list[-1][0] < inc_time:
            incoming_list.pop()
            continue
    if incoming_list:
        buff = buffer() # creation a package from the same time arrival messages
    else:
        while queue[first_index] != 0:
            first_index, free_space, packages_at_a_time = process_it(first_index, free_space, SIZE)
        break

    if buff[-1][1] == 0: # if there are zero duration pacakges and free queue, they will be processed immediately
        zero_dur_data(buff)

    if not buff: # if there is no items left in the buff, start receiving a new one
        continue

    if current_time >= buff[-1][0]:
        free_space, get_new_buff = put_on_stack(current_time, buff, free_space, SIZE, first_index)
        if get_new_buff:
            continue
        inc_time = current_time
    else:
        incoming_list.extend(buff)
    first_index, free_space, packages_at_a_time = process_it(first_index, free_space, SIZE)

for item in answer_list:
    print(item)