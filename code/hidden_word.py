from sys import stdin, stdout
import math


def read(): return stdin.readline().strip()
def read_int(): return map(int, read().split())
def write(s): stdout.write(s)


n, m, q = read_int()
a = [read() for _ in range(n)]
b = [set() for _ in range(11)]

h = min(10, n)
v = min(10, m)

for j in range(m):
    cur = 0
    for i in range(h):
        cur = 26 * cur + ord(a[i][j]) - 97
    b[h].add(cur)
    for i in range(h, n):
        cur = cur * 26 % (26 ** h) + ord(a[i][j]) - 97
        b[h].add(cur)

for i in range(n):
    cur = 0
    for j in range(v):
        cur = 26 * cur + ord(a[i][j]) - 97
    b[v].add(cur)
    for j in range(v, m):
        cur = cur * 26 % (26 ** v) + ord(a[i][j]) - 97
        b[v].add(cur)

s = [[] for _ in range(11)]
for i in range(q):
    t = read()
    cur = 0
    for c in t:
        cur = 26 * cur + ord(c) - 97
    s[len(t)].append((cur, i))

res = ['0' for _ in range(q)]
for i in reversed(range(11)):
    for t, p in s[i]:
        if t in b[i]:
            res[p] = '1'
        else:
            res[p] = '0'

    if i > 1:
        for c in b[i]:
            b[i - 1].add(c // 26)
            b[i - 1].add(c % (26 ** (i - 1)))
        b[i].clear()

write(''.join(res) + '\n')
