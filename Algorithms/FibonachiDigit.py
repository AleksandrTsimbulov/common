def fib_digit(n):
    fib_dig = []
    fib_dig.append(0)
    fib_dig.append(1)
    for i in range(2, n + 1):
        fib_dig.append((fib_dig[i - 1] + fib_dig[i - 2]) % 10)
    return fib_dig[n]



def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()