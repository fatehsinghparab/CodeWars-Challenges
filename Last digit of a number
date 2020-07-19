def last_digit(n1, n2):
    learn = []
    n1 = int(str(n1)[-1])
    if n1!=0!=n2:
            for i in range(1,10):
                pow_ = str(n1**i)[-1]
                if (pow_ not in learn):
                    learn.append(pow_)
                elif pow_ in learn:
                    break
            
            remainder = n2%4
            if remainder!=0:
                if remainder <= len(learn):
                    return int(learn[remainder-1])
                else:
                    if len(learn)!=1:
                        return int(learn[remainder-len(learn)-1])
                    else:
                        return int(learn[0])
            else:
                return int(learn[-1])
                  
    else:
        if n1 == 0 and n2!=0:
            return 0
        else:
            return 1
