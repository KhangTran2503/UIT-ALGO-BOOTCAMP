from sys import stdin, stdout


def read(): return stdin.readline().strip()
def read_int(): return [int(i) for i in read().split()]
def write(s): stdout.write(s)


n, = read_int()
a = read_int()

b = 1
for v in a:
    b = b << v | b

s = sum(a)
if s % 2 == 1:
    write('0')
elif b & (1 << (s // 2)) == 0:
    write('0')
else:
    p, v, i = -1, 1000, 0
    while i < n:
        c = 0
        while a[i] % 2 == 0:
            a[i] //= 2
            c += 1
        if c < v:
            v = c
            p = i
        i += 1
    write('1\n' + str(p + 1) + '\n')
