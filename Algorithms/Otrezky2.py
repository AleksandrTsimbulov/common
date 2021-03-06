# данная программа находит множество точек минимального размера, для которого каждый из
# отрезков содержит хотя бы одну точку
# введем количество отрезков n и сами отрезки


n = int(input())
segment_list = []
for number_of_segment in range(n):
    a, b = (int(i) for i in input().split())
    segment_list.append((a,b))

segment_list.sort(key=lambda i: i[1]) # отсортируем список в порядке возрастания вторых концов отрезков
#print(segment_list)
points = []
i = 0
while i < len(segment_list)-1:
    if segment_list[i][1] >= segment_list[i+1][0]:
        points.append(segment_list[i][1])
        del segment_list[i+1]
    else:
        points.append(segment_list[i][1])
        i += 1
# проверяем последний элемент из списка
different_points = set(points)
point_included = False
for number in range(segment_list[-1][0], segment_list[-1][1] + 1):
    if number in different_points:
        point_included = True
if not point_included:
    different_points.add(segment_list[-1][1])


print(len(different_points))
for point in different_points:
    print(point, end=' ')