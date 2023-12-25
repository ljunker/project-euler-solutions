multiple_3_5 = lambda x: x % 3 == 0 or x % 5 == 0

print(sum([x for x in range(1000) if multiple_3_5(x)]))