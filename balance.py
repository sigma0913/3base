import math

def to3(n):
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
        else:
            result = "T" + result
            n += 1

    return result

def from3(s):
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
            raise ValueError(f"err: {c}")

    return result

def add3(a, b):
    if str(a) == "1":
        if str(b) == "1":
            return "1T"
        elif str(b) == "T":
            return "0"
        else:
            return "1"
    elif str(a) == "T":
        if str(b) == "1":
            return "0"
        elif str(b) == "T":
            return "T1"
        else:
            return "T"
    else:
        return b

def sub3(a, b):
    if str(a) == "1":

        if str(b) == "1":
            return "0"
        
        elif str(b) == "0":
            return "1"
        
        else:
            return "1T"
        
    elif str(a) == "T":

        if str(b) == 1:
            return "T1"
        
        elif str(b) == 0:
            return "T"
        
        else:
            return "0"
    else:
        return str(a)

def mul3(a, b):
    if str(a) == "T":

        if str(b) == "1":
            return "T"
        
        elif str(b) == "0":
            return "0"
        
        else:
            return "1"
        
    elif str(a) == "1":
        return str(b)

    else:
        return "0"

