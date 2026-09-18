import math

def ToBalanced3(n):
    if n == 0:
        return "0"

    result = ""

    while n != 0:
        remainder = n % 3
        n //= 3

        if remainder == 0:
            result = "0" + result
        elif remainder == 1:
            result = "1" + result
        else:  # remainder == 2
            result = "T" + result
            n += 1

    return result

def FromBalanced3(s):
    result = 0

    for c in s:
        result *= 3

        if c == "1":
            result += 1
        elif c == "T":
            result -= 1
        elif c == "0":
            pass
        else:
            raise ValueError(f"不正な文字: {c}")

    return result


print(ToBalanced3(int(input())))


# for i in range(times):
#     num = [random.randint(10 ** (power -1), 10 ** power - 1), random.randint(10 ** (power - 1), 10 ** power - 1)]
#     print(str(bin(num[0])), str(bin(num[1])))