from Timer import timer


@timer
def solve():
    summe = 1000
    min_a, max_a = 1, summe // 3

    for a in range(1, max_a):
        for b in range(a + 1, (summe - a) // 2):
            c = summe - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


print(solve())
