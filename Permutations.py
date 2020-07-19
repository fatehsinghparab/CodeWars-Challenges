import itertools
def permutations(string):
    #print(string)
    if len(string) > 1:
        permute_ = list(set(["".join(i) for i in itertools.permutations(string,len(string))]))
        return permute_
    else:
        return list(string)
