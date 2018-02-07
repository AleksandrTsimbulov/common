import sys
from bisect import bisect_left, bisect_right
from timeit import default_timer as timer

start = timer()
reader = (tuple(map(int, line.split())) for line in sys.stdin)
n, m = next(reader)
segments = list(reader)
points = segments.pop()
seg_l = []
seg_r = []
for s in segments:
    seg_l.append(s[0])
    seg_r.append(s[1])
seg_l.sort()
seg_r.sort()
ans = []
end = timer()

start1 = timer()
for point in points:
    l = bisect_right(seg_l,point)
    r = bisect_left(seg_r, point)
    ans.append(l-r)
print(" ".join(str(i) for i in ans))
end1 = timer()
# print(end - start)
# print(end1 - start1)