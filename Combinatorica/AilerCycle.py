# Программа находит эйлеров цикл в графе
# по предоставленным количеством вершин и числу ребер
# организуем ввод графа
v, e = (int(i) for i in input().split()) # v - число вершин, e - число ребер графа
edge_list = []
for i in range(e):
    temp_list = [0,0]
    temp_list[0], temp_list[1] = (int(k) for k in input().split())
    edge_list.append(temp_list)
#print(edge_list)
# преобразуем запись данного графа из запиши по ребрам в запись "списка смежности"
adjacency_list = [[] for i in range(v+1)]
#print(adjacency_list)
for w in edge_list:
    adjacency_list[w[0]].append(w[1])
    adjacency_list[w[1]].append(w[0])
#print(adjacency_list)
del adjacency_list[0]
#print(adjacency_list)
#  выполним проверку графа на наличие эйлерова цикла, т.е. на связность и четность степеней вершин
is_connected_grath = False # изначально предположим, что граф не связный
is_no_odd_vertex = False # изнчально предположим, что в графе не все вершины имеют четную степень
is_cycle = False # изначально предположим что эйлерова цикла нет
# проверка графа на связность
# созданим список вершин
vertex_list = [int(i) for i in range(1,v+1)]
vertex_from_edges = []
for edge in edge_list:
    vertex_from_edges.append(edge[0])
    vertex_from_edges.append(edge[1])
set_vertex_from_edges = set(vertex_from_edges) # создадим множество, чтобы исключить повторы
if len(vertex_list) == len(set_vertex_from_edges):
    is_connected_grath = True
# проверка графа на четность степеней вершин
temporaty_counter = 0
if is_connected_grath:
    for vertex in adjacency_list:
        if len(vertex) % 2 != 0:
            temporaty_counter += 1
if temporaty_counter == 0:
    is_no_odd_vertex = True #в записи смежности для всех вершин четное д.б. четное кол-во эле-в
# если оба условия выполнены, цикл Эйлера есть
if is_no_odd_vertex and is_connected_grath:
    is_cycle = True

# поиск и вывод Эйлерова цикла
def cycle_fun(): # функция проходит один цикл и удаляет пройденные ребра
    cycle = False
    while cycle == False:
        for edge in edge_list:
            if edge[0] == have_been_vertexes[-1]:
                have_been_vertexes.append(edge[1])
                edge_list.remove(edge)
                break
            if edge[1] == have_been_vertexes[-1]:
                have_been_vertexes.append(edge[0])
                edge_list.remove(edge)
                break
        if have_been_vertexes[0] == have_been_vertexes[-1]:
            cycle = True
            del have_been_vertexes[-1]
        #print(have_been_vertexes)
        #print(edge_list)
    return

if is_cycle:
    # создадим список пройденных вершин
    have_been_vertexes = []
    start_vertex = edge_list[0][0] #введем первые вершины первого ребра
    second_vertex = edge_list[0][1]
    have_been_vertexes.append(start_vertex)
    have_been_vertexes.append(second_vertex)
    del edge_list[0] # удалим использованное ребро

    cycle_fun() # пройдем первый цикл
    while edge_list: # найдем новую начальную вершину для следующего цикла и будем повторять
                    # пока не пройдем все ребра, эта вершина должна принадлежать какому-то
                    # из не пройденных ребер
        for edge in edge_list:
            if edge[0] in have_been_vertexes:
                new_start_vertex = edge[0]
                new_second_vertex = edge[1]
                new_first_index = have_been_vertexes.index(new_start_vertex)
                new_second_index = have_been_vertexes.index(second_vertex)
                have_been_vertexes = (have_been_vertexes[new_first_index:] +
                                      have_been_vertexes[:new_first_index])
                have_been_vertexes.append(new_start_vertex)
                have_been_vertexes.append(new_second_vertex)
                edge_list.remove(edge)
                break
            if edge[1] in have_been_vertexes:
                new_start_vertex = edge[1]
                new_second_vertex = edge[0]
                new_first_index = have_been_vertexes.index(new_start_vertex)
                new_second_index = have_been_vertexes.index(second_vertex)
                have_been_vertexes = (have_been_vertexes[new_first_index:] +
                                      have_been_vertexes[:new_first_index])
                have_been_vertexes.append(new_start_vertex)
                have_been_vertexes.append(new_second_vertex)
                edge_list.remove(edge)
                break
        if edge_list:
            cycle_fun()

    for vertex in have_been_vertexes:
        print(vertex, end=' ')
else:
    print('NONE')