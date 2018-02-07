# Hoffman coding
# Illustrates naive greedy algorithm to code and decode small latin letters
s = input()
# ALFABIT = 'abcdefghijklmnopqrstuvwxyz'
temp_dict = {}
for letter in s:
    temp_dict[letter] = temp_dict.get(letter, 0) + 1
amount_of_diff_letters = len(temp_dict)

list_of_letters = list(temp_dict.items())
def getkey(item):
    return item[1]
list_of_letters.sort(key=getkey, reverse=True)
list_of_letters[0] = (list_of_letters[0][0], list_of_letters[0][1], '0')

for i in range(1, len(list_of_letters)):
    code =  '1'*i + '0'
    list_of_letters[i] = (list_of_letters[i][0], list_of_letters[i][1], code)

new_code = list_of_letters[-1][-1][:-2] + '1'
last_member = (list_of_letters[-1][0], list_of_letters[-1][1], new_code)
list_of_letters.pop()
list_of_letters.append(last_member)

temp_dict2 = {item[0]: item[-1] for item in list_of_letters}
coded_line = []
for letter in s:
    coded_line.append(temp_dict2[letter])
line_to_print = ''.join(coded_line)
print(amount_of_diff_letters, len(line_to_print))
for key, value in temp_dict2.items():
    print(key, value, sep=': ')
print(line_to_print)
# print(new_code)
# print(list_of_letters[-1][-1])
# print(temp_dict)
# print(list_of_letters)
# print(temp_dict2)