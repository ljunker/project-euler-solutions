from math import ceil, log

from Timer import timer


def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            yield i
            for n in range(i * i, limit + 1, i):
                nums[n] = False


def upper_bound(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


@timer
def find_n_prime(n):
    primes = list(find_primes(upper_bound(n)))
    return primes[n - 1]

print(upper_bound(10001))


print(find_n_prime(10001))
