def expanded_form(num):
    num = list(map(int,str(num)))
    zeros = len(num)-1
    sep = []
    print(num)
    for i in range(len(num)):
        if num[i]!=0:
            sep.append(num[i]*(10**zeros))
            zeros -=1
        else:
            zeros -=1
    zeros = ""
    for i in sep:
        zeros = zeros+" + "+str(i)
    return(str(zeros[3:]))
