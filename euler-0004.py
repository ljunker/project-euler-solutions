def is_palindrom(x):
    return x == x[::-1]


def generate_palindroms():
    for i in range(999):
        for j in range(999):
            number = (999 - i) * (999 - j)
            s = str(number)
            if is_palindrom(s):
                yield number


print(max([i for i in generate_palindroms()]))
