def find_outlier(integers):
    even = [i for i in integers if bin(i)[-1]=="0"]
    if len(even)==1:
        return even[0]
    elif sum(even) == sum(integers):
        return None
    else:
        return sum(integers) - sum(even)
