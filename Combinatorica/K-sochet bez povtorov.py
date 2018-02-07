k, n = (int(i) for i in input().split( ))
#print(k, n)
a = [i for i in range(0, n)]
#print(a)

def f(a,k):
    res = []
    if k == 0:
        res = []
    elif k == 1:
        for i in range(0, len(a)):
            res.append(a[i])
    elif k == len(a):
        for i in range(0, len(a)):
            res.append(a[i])
    else:
        b = f(a[1:], k-1)
        i = 0
        c = len(a) - 1
        while c > 0:
            b.insert(i, a[0])
            c -= 1
            i += 2
        res = b + f(a[1:],k)
    #print(res)
    return res

if k == 0:
    print(end='')
else:
    counter = 0
    for j in f(a,k):
        print(j, end=' ')
        counter += 1
        if counter % k == 0:
            print()




