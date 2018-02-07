# Hoffmancoding 2.0
# Illustrates another more correct hoffman algorithm
import heapq
import time

s = input()
temp_dict = {}
graph = []
for letter in s:
    temp_dict[letter] = temp_dict.get(letter, 0) + 1
amount_of_diff_letters = len(temp_dict)
#print(temp_dict)
ls = ''
left = None
right = None
for key, value in temp_dict.items():
    heapq.heappush(graph, (value, key, left, right, ls))
#print(graph)
for i in range(0, amount_of_diff_letters-1):
    left_merge = heapq.heappop(graph)
    right_merge = heapq.heappop(graph)
    new_value = left_merge[0] + right_merge[0]
    new_name = ''.join((left_merge[1], right_merge[1]))
    # print(new_name)
    left_merge_ls = list(left_merge)
    left_merge_ls[-1] = '0' + left_merge_ls[-1]
    right_merge_ls = list(right_merge)
    right_merge_ls[-1] = '1' + right_merge_ls[-1]
    heapq.heappush(graph, (new_value, new_name, left_merge_ls, right_merge_ls, ls))
# print(graph)

code_dict = {}
code_length = 0

def get_code(object, code_start=''):
    new_code = ''.join((code_start, object[4]))
    if object[2] is None:
        code_dict.update({object[1] : new_code})
    else:
        get_code(object[2], new_code)
        get_code(object[3], new_code)

def get_length(object):
    global code_length
    code_length += object[0]
    if object[2]:
        get_length(object[2])
        get_length(object[3])

if amount_of_diff_letters > 1:
    get_code(graph[0])
    get_length(graph[0])
    code_length -= graph[0][0]
else:
    code_dict = {graph[0][1] : '0'}
    code_length = len(s)
coded_string_ls=[]
for letter in s:
    coded_string_ls.append(code_dict[letter])
coded_string = ''.join(coded_string_ls)
print(amount_of_diff_letters, code_length)
for key, item in code_dict.items():
    print(key, item, sep=': ')
print(coded_string)
