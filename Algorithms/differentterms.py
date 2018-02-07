# Different terms
# Illustrates some naive greedy algorithms
#import sys

#input = sys.stdin
n = int(input())
list_of_terms = []
while n:
    temp_sum = 0
    for i in range(1, n+1):
        temp_sum += i
        if temp_sum == n:
            list_of_terms.extend(range(1, i+1))
            n -= temp_sum
            break
        elif temp_sum > n:
            list_of_terms.extend(range(1, i+1))
            difference = temp_sum - n
            list_of_terms.remove(difference)
            n = 0
            break
print(len(list_of_terms))
print(" ".join([str(i) for i in list_of_terms]))


