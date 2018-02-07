# Find text
# Realization of Rabina-Karpa algorithm

import sys


def raised_in(number, power, p):
    result = 1
    for i in range(power):
        result = (result * number) % p
    return result % p


def hashfunc(string):
    global P
    global X
    i = 0
    summa = 0
    for char in string.encode('ascii'):
        summa += (char * raised_in(X, i, P)) % P
        i += 1
    hash_number = summa % P
    return hash_number


def shifthash(prev_hash, last_letter, new_letter):
    global X_in_power_pattern
    global P
    global X
    enclosures = ((prev_hash - ord(last_letter) * X_in_power_pattern) % P + P) % P
    result = ((enclosures * X) % P + ord(new_letter)) % P
    return result



data = sys.stdin
reader = (line.strip() for line in data)
patttern = next(reader)
text_line = next(reader)
P = 1000000007 # prime number
X = 263 # constant for hashing
len_p = len(patttern)
X_in_power_pattern = raised_in(X, len_p-1, P)
hash_pattern = hashfunc(patttern)
start_index = len(text_line) - len_p
first_hash = hashfunc(text_line[start_index:])
ans = []

if first_hash == hash_pattern:
    if patttern == text_line[start_index:]:
        ans.append(start_index)

last_letter = text_line[-1]
start_index -= 1
prev_hash = first_hash

while start_index >= 0:
    current_hash = shifthash(prev_hash, last_letter, text_line[start_index])
    # print(current_hash, hash_pattern, prev_hash, patttern, text_line[start_index:start_index+len_p], start_index, last_letter)
    if current_hash == hash_pattern:
        if patttern == text_line[start_index:start_index+len_p]:
            ans.append(start_index)
    start_index -= 1
    prev_hash = current_hash
    last_letter = text_line[start_index+len_p]


while ans:
    print(ans.pop(), end=' ')
