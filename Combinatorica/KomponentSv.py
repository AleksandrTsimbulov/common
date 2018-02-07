# Данная программа находит количество компонент связности неориентированного графа при помощи
# поиска в грубину

# зададим число вершин v и число ребер e
v, e = (int(i) for i in input().split())

# задаем граф списком ребер, их количество равно e
edges_list = []
for m in range(e):
    current_edge = [0, 0]
    current_edge[0], current_edge[1] = (int(i) for i in input().split())
    edges_list.append(current_edge)


def dfs(vertex):
    visited[vertex] = True
    for i in edges_list:
        if i[0] == vertex:
            if not visited[i[1]]:
                dfs(i[1])
        elif i[1] == vertex:
            if not visited[i[0]]:
                dfs(i[0])



visited = [False] * (v+1)
number_of_components = 0
for ver in range(1,v+1):
    if not visited[ver]:
        dfs(ver)
        number_of_components += 1

print(number_of_components)
