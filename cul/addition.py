import random
import math
import balance

times = int(input("times: "))
power = int(input("power: "))

for i in range(times):
    num = [random.randint(10 ** (power -1), 10 ** power - 1), random.randint(10 ** (power - 1), 10 ** power - 1)]
    print(str(bin(num[0])), str(bin(num[1])))
    print(str(balance.to3(num[0])), str(balance.to3(num[1])))