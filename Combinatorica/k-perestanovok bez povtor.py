# Задача на генерацию всех возможных к-перестановок из n элементов
# на вход подается два числа k и n, для них гарантированно, что 0<=k<=n
# на выходе должно быть необходимое число лексикографически упорядоченных строк
# из k чисел от 0 до n-1, разделенных пробелом

# организовываем ввод чисел и создаем исходный список

n, k = (int(i) for i in input().split())
myList = list(range(n))
print(myList)

def func_list(list, k):
    if k != 1:
        for element in list:
            new_list = list[:]
            new_list.remove(element)
            temp = []
            temp = func_list(new_list, k-1)
            for i in range(0, len(temp), k-1):
                temp.insert(i, element)
        result = temp

    else:
        result = list[:]
    return result


