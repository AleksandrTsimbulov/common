# The priority queue
# Illustrates the priority queue  realization
import sys
import math

priority_queue = []
last_index = - 1

def insertNumber(number):
    global last_index
    priority_queue.append(number)
    last_index += 1
    current_index = last_index
    parent_index = math.floor(current_index / 2)
    while priority_queue[current_index] > priority_queue[parent_index]:
        priority_queue[current_index], priority_queue[parent_index] = (
        priority_queue[parent_index], priority_queue[current_index]
        )
        current_index = math.floor(current_index / 2)
        parent_index = math.floor(current_index / 2)

def extractMax():
    global last_index
    if last_index == 0:
        print(priority_queue.pop())
        last_index -= 1
        return
    priority_queue[0], priority_queue[last_index] = (
        priority_queue[last_index], priority_queue[0]
    )
    print(priority_queue.pop())
    current_index = 0
    last_index -= 1
    first_child_index = 2 * current_index
    second_child_index = 2 * current_index + 1
    if first_child_index >= last_index:
        if first_child_index == last_index:
            if priority_queue[current_index] < priority_queue[first_child_index]:
                priority_queue[current_index], priority_queue[first_child_index] = (
                    priority_queue[first_child_index], priority_queue[current_index]
                )
                return
            else:
                return
        else:
            return
    while (priority_queue[current_index] < priority_queue[first_child_index] or
    priority_queue[current_index] < priority_queue[second_child_index]):
        if priority_queue[first_child_index] >= priority_queue[second_child_index]:
            priority_queue[current_index], priority_queue[first_child_index] = (
                priority_queue[first_child_index], priority_queue[current_index]
            )
            current_index = 2 * current_index
            first_child_index = 2 * current_index
            second_child_index = 2 * current_index + 1
            if first_child_index >= last_index:
                if first_child_index == last_index:
                    if priority_queue[current_index] < priority_queue[first_child_index]:
                        priority_queue[current_index], priority_queue[first_child_index] = (
                            priority_queue[first_child_index], priority_queue[current_index]
                        )
                        return
                    else:
                        return
                else:
                    return
        else:
            priority_queue[current_index], priority_queue[second_child_index] = (
                priority_queue[second_child_index], priority_queue[current_index]
            )
            current_index = 2 * current_index + 1
            first_child_index = 2 * current_index
            second_child_index = 2 * current_index + 1
            if first_child_index >= last_index:
                if first_child_index == last_index:
                    if priority_queue[current_index] < priority_queue[first_child_index]:
                        priority_queue[current_index], priority_queue[first_child_index] = (
                            priority_queue[first_child_index], priority_queue[current_index]
                        )
                        return
                    else:
                        return
                else:
                    return

input = sys.stdin
n = int(input.readline())
for i in range(n):
    command = input.readline()
    if "Insert" in command:
        inserted_number = int(command.split()[1])
        insertNumber(inserted_number)
        #print(priority_queue)
    elif "ExtractMax" in command:
        extractMax()
        #print(priority_queue)
