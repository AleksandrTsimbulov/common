import sys


data = sys.stdin
reader = (line.strip() for line in data)
hash_table_size = int(next(reader))
n_requests = int(next(reader))
P = 1000000007  # prime number
X = 263  # constant for hashing

hash_table = [[] for i in range(hash_table_size)]


def hashfunc(string):
    global P
    global X
    global hash_table_size
    summa = 0
    i = 0
    for character in string.encode('ascii'):
        multiplier = (X**i) % P
        summa += (character * multiplier) % P
        summa = summa % P
        i += 1
    hash_number = summa % hash_table_size
    return hash_number


for i in range(n_requests):
    request = next(reader)
    if request.startswith('add'):
        add,string = request.split()
        hash_key = hashfunc(string)
        if string not in hash_table[hash_key]:
            hash_table[hash_key].insert(0, string)
    elif request.startswith('del'):
        del_request, string = request.split()
        hash_key = hashfunc(string)
        if string in hash_table[hash_key]:
            hash_table[hash_key].remove(string)
    elif request.startswith('find'):
        find_request, string = request.split()
        hash_key = hashfunc(string)
        if string in hash_table[hash_key]:
            print('yes')
        else:
            print("no")
    elif request.startswith('check'):
        check_it, index = request.split()
        index = int(index)
        if hash_table[index]:
            print(' '.join(hash_table[index]))
        else:
            print()