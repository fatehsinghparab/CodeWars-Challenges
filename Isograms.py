def is_isogram(string):
    #your code here
    string = list(map(ord,str(string).lower()))
    return len(string)==len(set(string))
