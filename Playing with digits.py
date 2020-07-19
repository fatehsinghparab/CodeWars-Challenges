import math
def dig_pow(n, p):
    N = n
    n = [int(i) for i in str(n)]
    sum = 0
    for i in range(len(n)):
        sum = sum + n[i]**(p+i)
    final = sum/N
    if math.modf(final)[0]==0:
        return final
    else:
        return -1
