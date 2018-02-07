# Hoffman decoding
# Illustrates naive decoding algorithm converting bit string into small letters
import sys

input = sys.stdin
k, l = map(int, input.readline().rstrip().split())
decod_dict = {}
for i in range(k):
    value, key = input.readline().rstrip().split(': ')
    decod_dict.update({key : value})
encoded_string = input.readline().rstrip()
encoded_list = list(encoded_string)
encoded_list.reverse()
decoded_list = []
letter_code = ''
while encoded_list:
    letter_code = ''.join((letter_code, encoded_list.pop()))
    if letter_code in decod_dict:
        decoded_list.append(decod_dict[letter_code])
        letter_code = ''
print(''.join(decoded_list))
# print(decod_dict)
# print(encoded_string)
# print(encoded_list)
