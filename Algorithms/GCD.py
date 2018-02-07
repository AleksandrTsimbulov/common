def gcd(a, b):
    d = 0
    if a == 0:
        d = b
    elif b == 0:
        d = a
    else:
        if a >= b:
            d = gcd(a % b, b)
        else:
            b >= a
            d = gcd(a, b % a)
    return d



def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()