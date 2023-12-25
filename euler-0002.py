def fib(max_amount):
    current = 0
    fib_0 = 0
    fib_1 = 1
    while current <= max_amount:
        current = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = current
        if current <= max_amount:
            yield current


print(sum([x for x in fib(4000000) if x % 2 == 0]))
