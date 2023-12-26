from math import lcm

# smallest number divisible by list is just lcm(list)
i = lcm(*[x for x in range(1, 20)])

print(i)
