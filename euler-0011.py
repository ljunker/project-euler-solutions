from functools import reduce
from operator import mul

grid = [[int(x) for x in line.split()] for line in open("euler-0011-input.txt").readlines()]
print(grid)


def horizontal(grid, run_len):
    max_prod = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m - run_len + 1):
            subset = grid[i][j:j + run_len]
            product = reduce(mul, subset, 1)
            max_prod = max(max_prod, product)
    return max_prod


def vertical(grid, run_len):
    max_prod = 0
    n, m = len(grid), len(grid[0])
    for i in range(n - run_len + 1):
        for j in range(m):
            product = 1
            for k in range(run_len):
                product *= grid[i + k][j]
            max_prod = max(max_prod, product)
    return max_prod


def diagonal_natural(grid, run_len):
    max_prod = 0
    n, m = len(grid), len(grid[0])
    for i in range(n - run_len + 1):
        for j in range(m - run_len + 1):
            product = 1
            for k in range(run_len):
                product *= grid[i + k][j + k]
            max_prod = max(max_prod, product)
    return max_prod


def diagonal_reverse(grid, run_len):
    max_prod = 0
    n, m = len(grid), len(grid[0])
    for i in range(run_len - 1, n):
        for j in range(m - run_len + 1):
            product = 1
            for k in range(run_len):
                product *= grid[i - k][j + k]
            max_prod = max(max_prod, product)
    return max_prod


def solve():
    run_len = 4
    max_prods = [horizontal(grid, run_len), vertical(grid, run_len),
                 diagonal_natural(grid, run_len), diagonal_reverse(grid, run_len)]

    answer = max(max_prods)
    return answer


print(solve())
