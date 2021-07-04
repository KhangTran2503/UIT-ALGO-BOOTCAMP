import numpy as np
import os
import itertools
import subprocess as sp
import random

id = '146'
sol = os.path.join(id, 'sol')
inp = os.path.join(id, 'in')
out = os.path.join(id, 'out')


def gen_random(n: int): return ''.join(
    map(chr, np.random.randint(97, 97 + 26, n)))


def write(path, data: list):
    with open(path, 'w') as file:
        for line in data:
            file.write(line + '\n')


def gen_all(n: int): return [''.join(v)
                             for v in itertools.permutations(gen_random(n))]


def write_test(i: int, data: list):
    inp_path = os.path.join(inp, str(i) + '.txt')
    out_path = os.path.join(out, str(i) + '.txt')

    write(inp_path, data)

    args = [sol]
    inp_file = open(inp_path, 'r')
    out_file = open(out_path, 'w')

    runner = sp.run(args=args, stdin=inp_file, stdout=out_file)


def make_tests():
    if not os.path.exists(inp):
        os.makedirs(inp)
    if not os.path.exists(out):
        os.makedirs(out)

    for i in range(1, 11):
        data = []
        for _ in range(1, 10000):
            data.append(gen_random(i * 5))
        random.shuffle(data)
        data.append('#')

        write_test(i, data)

        data.clear()

    for i in range(11, 101):
        data = gen_all(9)
        random.shuffle(data)
        data.append('#')

        write_test(i, data)

        data.clear()


make_tests()
