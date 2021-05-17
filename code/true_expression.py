from sys import stdin, stdout
import math


def read(): return stdin.readline().strip()
def read_int(): return map(int, read().split())
def write(s): stdout.write(s)


n, s = read_int()

if s % 2 != n * (n + 1) // 2 % 2:
    write("NO_SOLUTION\n")
elif n * (n + 1) // 2 < s:
    write("NO_SOLUTION\n")
else:
    res = ['+' for _ in range(n)]
    s = (n * (n + 1) // 2 - s) // 2
    for i in reversed(range(n)):
        if i < s:
            s -= i + 1
            res[i] = '-'
    write(''.join(res) + '\n')
