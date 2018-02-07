# данная программа выводит список из V чисел - расстояний от вершины 0 до соответстующих
# вершин графа

# организуем ввод графа
v, e = (int(i) for i in input().split()) # v - число вершин, e - число ребер графа
edge_list = []
for i in range(e):
    temp_list = [0,0]
    temp_list[0], temp_list[1] = (int(k) for k in input().split())
    edge_list.append(temp_list)


# преобразуем запись данного графа из запиши по ребрам в запись "списка смежности"
adjacency_list = [[] for i in range(v)]
for w in edge_list:
    adjacency_list[w[0]].append(w[1])
    adjacency_list[w[1]].append(w[0])
#print(adjacency_list)

colored = [False]*v #список посещенных вершин
initial_root_number = 0 # корневой элемент дерева, в нашем случае 0
queue = [] # создадим список для очереди
distance = [0]*v # создадим список расстояний
counter = 1 # счетчик расстояния
colored[initial_root_number] = True
distance[initial_root_number] = 0

for i in adjacency_list[initial_root_number]:
    if not colored[i]:
        queue.append(i)
        distance[i] = counter
        colored[i] = True
counter += 1
#print(queue)


def fanct(queue):
    global counter
    new_queue = []
    while queue:
        temp_number = queue.pop(0)
        for w in adjacency_list[temp_number]:
            if not colored[w]:
                new_queue.append(w)
                distance[w] = counter
                colored[w] = True
    counter += 1
    for elements in colored:
        if not elements:
            fanct(new_queue)
    return

fanct(queue)

for i in distance:
    print(i, end=' ')

