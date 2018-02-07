import sys

reader = sys.stdin
q = tuple(map(int, reader.readline().strip()))[0]
incoming_list = [line.strip() for line in reader]
MAX = 'max'
PUSH = 'push'
POP = 'pop'


def getnumber(string):
    number = int(tuple(string.split())[1])
    return number

maxstack = []
for requests in incoming_list:
    if PUSH in requests:
        number = getnumber(requests)
        if maxstack:
            if number >= maxstack[-1]:
                maxstack.append(number)
            else:
                maxstack.append(maxstack[-1])
        else:
            maxstack.append(number)
    elif POP in requests:
        maxstack.pop()
    elif MAX in requests:
        print(maxstack[-1])
