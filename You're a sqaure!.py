import math
def is_square(n):    
    try:
        if (math.modf((n)**(1/2)))[0] == 0 :
            return True
        else:
            return False
    except:
        return False
