import math

def who_is_next(names, r):
    n = len(names)
    k = 2 ** int(math.log(1 + (r - 1) // n, 2))
    s = 1 + (k - 1) * n
    return names[(r - s) // k]
