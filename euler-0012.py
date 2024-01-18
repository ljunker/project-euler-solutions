import math

from Timer import timer


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def triangle_number_generator():
    number = 1
    count = 1
    while True:
        number = number + count
        count = count + 1
        yield number


@timer
def solve():
    gen = triangle_number_generator()
    while True:
        i = next(gen)
        x = list(divisorGenerator(i))
        if len(x) > 500:
            print(f'found it: {i}')
            break


solve()
