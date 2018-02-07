def fib_mod(n, m):
    fib_dig = []
    fib_dig.append(0)
    fib_dig.append(1)
    amount = 2
    for i in range(2, n*6):
        fib_dig.append((fib_dig[i - 1] + fib_dig[i - 2]) % m)
        amount += 1
        if (fib_dig[i] == 1) and (fib_dig[i-1] == 0):
            amount -= 2
            break

    return fib_dig[(n%amount)]



def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()