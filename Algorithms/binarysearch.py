# Binary search
# Illustrates naive binary search algorithm
import sys

def get_data():
    # generator of tuple of integers from the line in sys.stdin
    # each time it's called it returns a tuple of int numbers
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # below is an example of usage
    n_massive = []
    for item in next(reader):
        n_massive.append(item)
    k_massive = []
    for item in next(reader):
        k_massive.append(item)
    n = n_massive.pop(0)
    k = k_massive.pop(0)
    assert len(n_massive) == n
    assert len(k_massive) == k
    return n, k, n_massive, k_massive

def print_index_if_exist(n, k, n_massive, k_massive):
    # prints index if object with index k in massive k_massive exist in n_massive else "-1"
    NOT_EXIST = -1
    max_n_search_index = n - 1
    min_n_search_index = 0
    def search(searching_item, min_n_search_index, max_n_search_index):
        middle_index = (min_n_search_index + max_n_search_index) // 2
        if n_massive[middle_index] == searching_item:
            return print(middle_index + 1, end=' ')
        elif n_massive[middle_index] > searching_item:
            new_max_n_search_index = middle_index - 1
            if new_max_n_search_index < min_n_search_index:
                return print(NOT_EXIST, end=' ')
            else:
                search(searching_item, min_n_search_index, new_max_n_search_index)
        elif n_massive[middle_index] < searching_item:
            new_min_n_search_index = middle_index + 1
            if new_min_n_search_index > max_n_search_index:
                return print(NOT_EXIST, end=' ')
            else:
                search(searching_item, new_min_n_search_index, max_n_search_index)
    for i in range(k):
        searching_item = k_massive[i]
        search(searching_item, min_n_search_index, max_n_search_index)

def main():
    n, k, n_massive, k_massive = get_data()
    # print(n, k, n_massive, k_massive)
    print_index_if_exist(n, k, n_massive, k_massive)

main()

# incoming_data = sys.stdin
# n, a* = map(int, incoming_data.readline().split())