import sys
from bisect import bisect, bisect_left
# from timeit import default_timer as timer

def getdata():
    data = sys.stdin
    n, m = map(int, data.readline().split())
    list_of_sections = []
    for i in range(n):
        a, b = map(int, data.readline().split())
        list_of_sections.append((a, b))
    list_of_numbers = [int(i) for i in data.readline().split()]
    list_of_numbers.reverse()
    # print(list_of_sections)
    assert len(list_of_numbers) == m
    assert len(list_of_sections) == n
    list_of_sections.sort()
    return n, m, list_of_numbers, list_of_sections


def main():
    # start = timer()
    n, m, list_of_numbers, list_of_sections = getdata()
    # end = timer()
    # start1 = timer()
    number_of_points = []
    while list_of_numbers:
        m_number = list_of_numbers.pop()
        m_index_right = bisect(list_of_sections[0], m_number)
        m_index_left = bisect_left(list_of_sections[1], m_number)
        number_of_points.append(str(m_index_right - m_index_left))
    print(" ".join(str(i) for i in number_of_points))
    # end1 = timer()
    # print('\n', end - start, sep='')
    # print(end1 - start1)

main()