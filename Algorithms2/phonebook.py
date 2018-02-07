import sys

data = sys.stdin
reader = (line.strip() for line in data)

n = int(next(reader))
max_phone_number = 9999999 + 1

hash_table = [0*i for i in range(max_phone_number)]

for i in range(n):
    request = next(reader)
    if "add" in request:
        add, number, name = request.split()
        hash_key = int(number)
        hash_table[hash_key] = name
    elif "del" in request:
        del_request, number = request.split()
        hash_key = int(number)
        if hash_table[hash_key] != 0:
            hash_table[hash_key] = 0
    elif "find" in request:
        find_request, number = request.split()
        hash_key = int(number)
        if hash_table[hash_key] != 0:
            print(hash_table[hash_key])
        else:
            print("not found")