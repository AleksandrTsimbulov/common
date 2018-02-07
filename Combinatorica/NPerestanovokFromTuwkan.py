n,k =map(int, input().split())
allelement = [i for i in range(n)]

def printkfromn(start, now, spis=[]):
    if now != k:
        temp = spis
        for elem in range(start,n):
            #print(elem)
            if elem not in temp:
                temp.append(allelement[elem])
                printkfromn(start, now+1,temp)
                temp.pop()
    else:
        for element in range(start, n):
            if element not in spis:
                for j in spis:
                    print(j, end=' ')
                print(element)

if k !=0:
    printkfromn(0,1)