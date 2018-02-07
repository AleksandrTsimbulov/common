def fib(n):
    # put your code here
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2, n+1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n]
def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()


'''

n = 3
fib_list = []
fib_list.append(0)
fib_list.append(1)
for i in range(2, n+1):
    fib_list.append(fib_list[i-1] + fib_list[i-2])
print(fib_list[n])
'''