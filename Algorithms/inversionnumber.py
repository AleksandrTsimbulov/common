# Inversion number
# Illustrates O(nlog(n)) algorithm for counting the amount of inversed numbers in row
import sys

def get_data():
    # generator of tuple of integers from the line in sys.stdin
    # each time it's called it returns a tuple of int numbers from one line
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # below is an example of usage
    n = next(reader)[0]
    massive_n = [[item] for item in next(reader)]
    assert len(massive_n) == n
    return n, massive_n

def merge_massive(massive_a, massive_b):
    # while merging two massives counts inversions
    merged_massive = []
    global counter
    massive_a = massive_a[::-1]
    massive_b = massive_b[::-1]
    while True:
        if massive_a[-1] <= massive_b[-1]:
            merged_massive.append(massive_a.pop())
            if not massive_a:
                while massive_b:
                    merged_massive.append(massive_b.pop())
                break
        else:
            counter += len(massive_a)
            merged_massive.append(massive_b.pop())
            if not massive_b:
                while massive_a:
                    merged_massive.append(massive_a.pop())
                break
    return merged_massive

def all_go_thrmass(massive):
    # recursevly go through massive and merge pairs of elements
    updated_massive = []
    i = 0
    last_index = len(massive) - 1
    # print(last_index)
    while i + 1 <= last_index:
        updated_massive.append(merge_massive(massive[i], massive[i+1]))
        i += 2
        # print(i, i+1 < last_index, updated_massive)
    if i == last_index:
        updated_massive.append(massive[last_index])
    if len(updated_massive) > 1:
        # print(updated_massive)
        all_go_thrmass(updated_massive)

def naive_algorithm(massive):
    count = 0
    while massive:
        first = massive.pop(0)
        for element in massive:
            if first > element:
                count += 1
    return count

def main():
    n, massive_n = get_data()
    # print(massive_n)
    all_go_thrmass(massive_n)
    # print(naive_algorithm(massive_n))



counter = 0
main()
print(counter)




