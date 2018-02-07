# данная программа находит множество точек минимального размера, для которого каждый из
# отрезков содержит хотя бы одну точку
# введем количество отрезков n и сами отрезки
n = int(input())
segment_list = []
for number_of_segment in range(n):
    a, b = (int(i) for i in input().split())
    segment_list.append([a,b])

segment_list.sort(key=lambda i: i[1]) # отсортируем список в порядке возрастания вторых концов отрезков
#print(segment_list)
points = []
cont_of_process = True
i = 0
while i < len(segment_list)-1:
    if segment_list[i][1] >= segment_list[i+1][0]:
        if segment_list[i][1] not in points:
            points.append(segment_list[i][1])
        del segment_list[i+1]
    else:
        if segment_list[i][1] not in points:
            points.append(segment_list[i][1])
        i += 1
# проверяем последний элемент из списка
point_included = False
for number in range(segment_list[-1][0], segment_list[-1][1] + 1):
    if number in points:
        point_included = True
if not point_included:
    points.append(segment_list[-1][1])


print(len(points))
for point in points:
    print(point, end=' ')


