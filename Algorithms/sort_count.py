import sys

reader = sys.stdin
n = map(int, reader.readline())
number_lst = tuple(map(int, reader.readline().split()))
dict = {}
for item in number_lst:
    dict[item] = dict.get(item, 0) + 1
answer_list = []
for key, value in sorted(dict.items()):
    answer_list.extend([str(key)] * value)
print(" ".join(answer_list))

