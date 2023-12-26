from itertools import islice
from math import prod

line = list(open("euler-0008-input.txt").readline())
line = [int(i) for i in line]


def window(seq, n=2):
    it = iter(seq)
    result = list(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + [elem, ]
        yield result


windows = list(window(line, 13))
print(max([prod(l) for l in windows]))
