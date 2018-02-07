import sys

data = sys.stdin
reader = (line.strip() for line in data)
patttern = next(reader)
text_line = next(reader)
d = 26
q = 1000007
ans = []
n = len(text_line)
m = len(patttern)
h = d**(m-1) % q
p = 0
t0 = 0

for i in range(0, m):
    p = (d*p + ord(patttern[i])) % q
    t0 = (d*t0 + ord(text_line[i])) % q
ts = t0
for s in range(0, n-m+1):
    if p == ts:
        if patttern == text_line[s:s+m]:
            ans.append(s)
    if s < n-m:
        ts = (d*(ts - ord(text_line[s]) * h) + ord(text_line[s + m])) % q

print(' '.join(str(i) for i in ans))