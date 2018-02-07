import math
def binomial(n,k):
    result = (math.factorial(n))//(math.factorial(k)*math.factorial(n - k))
    #print(result)
    return result

n = int(input())
k = int(input())

answer = []
for i in range(0, k+1):
    answer.append((pow(-1, k-i) * binomial(k, i) * pow(i, n)))
    print(i)
    print(pow(-1, k-i))
    print(binomial(k, i))
    print(pow(i, n))
    print(answer)


print(answer)
c = 0
for b in answer:
    c += b
print(c)