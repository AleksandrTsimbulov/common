#import string
import sys

#input = open('1.txt', 'r') # расскомментировать решая задачу локально
input = sys.stdin #расскомментировать при сдаче задачи в системе
S = []
n = int(input.readline())
for i in range(1,n+1):
  x,y = map(int, input.readline().split())
  S.append([x,y])
#input.close()

def getKey(item):
    return item[1]
S.sort(key=getKey)

print(S)
point = S[0][1]
point_list = []
point_list.append(point)
counter = 1
while S:
    if S[0][0] <= point:
        S.pop(0)
    else:
        point = S[0][1]
        counter += 1
        point_list.append(point)
        S.pop(0)

print(counter)
for element in point_list:
    print(element, end=" ")



# 19
# 102 188 242 270 294 340 390 432 452 480 498 652 661 692 738 780 839 937 978
