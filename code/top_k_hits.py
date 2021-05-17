from sys import stdin, stdout


def read(): return stdin.readline().strip()
def read_int(): return [int(i) for i in read().split()]
def write(s): stdout.write(s)


n, q = read_int()
N, B, E = 1 << 16, 1, n

seg = [[] for i in range(N << 1)]
laz = [0 for i in range(N << 1)]


def _upd(i: int, add: int):
    global seg, laz
    for id in range(len(seg[i])):
        seg[i][id] = (seg[i][id][0] + add, seg[i][id][1])
    laz[i] += add


def merge(i: int):
    global seg, laz
    seg[i].clear()
    x, y, i1, i2 = 0, 0, i << 1, i << 1 | 1
    while len(seg[i]) < 5 and (x < len(seg[i1]) or y < len(seg[i2])):
        if x == len(seg[i1]):
            seg[i].append(seg[i2][y])
            y += 1
        elif y == len(seg[i2]):
            seg[i].append(seg[i1][x])
            x += 1
        elif seg[i2][y] >= seg[i1][x]:
            seg[i].append(seg[i2][y])
            y += 1
        else:
            seg[i].append(seg[i1][x])
            x += 1


def push(i: int):
    global seg, laz
    i1, i2 = i << 1, (i << 1) | 1
    _upd(i1, laz[i])
    _upd(i2, laz[i])
    merge(i)
    laz[i] = 0


def upd(l: int, r: int, add: int, i: int = 1, b: int = B, e: int = E):
    global seg, laz
    if b > r or e < l:
        return
    if l <= b and e <= r:
        _upd(i, add)
        return
    if laz[i] != 0:
        push(i)
    m = (b + e) >> 1
    upd(l, r, add, i << 1, b, m)
    upd(l, r, add, (i << 1) | 1, m + 1, e)
    merge(i)


def build(i: int = 1, b: int = B, e: int = E):
    global seg, laz
    if b == e:
        seg[i] = [(0, b)]
        return
    m = (b + e) >> 1
    build(i << 1, b, m)
    build((i << 1) | 1, m + 1, e)
    merge(i)


build()

for _ in range(q):
    t = read_int()
    if len(t) == 4:
        _, l, r, v = t
        upd(l, r, v)
    else:
        _, k = t
        k = min(k, n)
        for i in range(k):
            write(str(seg[1][i][1]) + ('\n' if i == k - 1 else ' '))