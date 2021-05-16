from sys import stdin, stdout


def read(): return stdin.readline().strip()
def read_int(): return [int(i) for i in read().split()]
def write(s): stdout.write(s)


def test(i: int, j: int):
    global near, bomb, n, m, remain

    if i <= 0 or i > n or j <= 0 or j > m:
        return

    cnt = 0
    cur = near[i][j]
    for k in [-1, 1]:
        cnt += bomb[i + k][j] == -1
        cnt += bomb[i][j + k] == -1
        cur -= bomb[i + k][j] == 1
        cur -= bomb[i][j + k] == 1

    if cnt == 0:
        return

    if cur == 0:
        for k in [-1, 1]:
            if bomb[i + k][j] == -1:
                bomb[i + k][j] = 0
                remain -= 1
                test(i + k + k, j)
            if bomb[i][j + k] == -1:
                bomb[i][j + k] = 0
                remain -= 1
                test(i + k + k, j)
    elif cur == cnt:
        for k in [-1, 1]:
            if bomb[i + k][j] == -1:
                bomb[i + k][j] = 1
                remain -= 1
                test(i + k + k, j)
            if bomb[i][j + k] == -1:
                bomb[i][j + k] = 1
                remain -= 1
                test(i + k + k, j)


n, m = read_int()
near = [[0 for _ in range(m + 2)]] + [[0] + read_int() + [0]
                                      for _ in range(n)] + [[0 for _ in range(m + 2)]]
bomb = [[0 for _ in range(m + 2)]] + \
    [[0] + [-1 for _ in range(m)] + [0]
     for _ in range(n)] + [[0 for _ in range(m + 2)]]

remain = n * m
while remain > 0:
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            test(i, j)

for i in range(1, n + 1):
    write(' '.join([str(bomb[i][j]) for j in range(1, m + 1)]) + '\n')
