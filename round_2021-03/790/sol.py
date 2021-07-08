from sys import stdin, stdout
import math


def read(): return stdin.readline().strip()
def read_int(): return [int(i) for i in read().split()]
def write(s): stdout.write(s)


def convert(line):
    line = line.strip().split(' ')
    line[0] = int(line[0])
    line[1] = ord(line[1]) - 65
    line[2] = int(line[2].split(':')[0]) * 60 + int(line[2].split(':')[1])
    line[3] = line[3] == 'Y'
    return line


def add(a, log):
    no, id, tm, st = log

    if no not in a:
        a[no] = {'no': no, 'cnt': 0, 'tm': 0,
                 'sol': [0 for _ in range(26)], 'rk': 0}

    if a[no]['sol'][id] != -1:
        if st:
            a[no]['tm'] += tm + 20 * a[no]['sol'][id]
            a[no]['sol'][id] = -1
            a[no]['cnt'] += 1
        else:
            a[no]['sol'][id] += 1


data = stdin.readlines()
data = list(map(convert, data))

a = dict()
for log in data:
    add(a, log)

a = list(a.values())
a.sort(key=lambda log: 1000 * log['cnt'] - log['tm'], reverse=True)

crk, csol, ctm = 0, 1000, 0
for i in range(len(a)):
    if csol != a[i]['cnt'] or ctm != a[i]['tm']:
        crk = i + 1
        csol = a[i]['cnt']
        ctm = a[i]['tm']
    a[i]['rk'] = crk

for i in range(len(a)):
    if a[i]['sol']:
        print(a[i]['rk'], a[i]['no'], a[i]['cnt'], a[i]['tm'])
    else:
        print(a[i]['id'], a[i]['no'])