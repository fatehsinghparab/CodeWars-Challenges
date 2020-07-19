def iq_test(numbers):
    #your code here
    numbers= list(enumerate(map(float,(numbers.split())),1))
    #print(numbers)
    even = []
    odd = []
    for i in numbers:
        if i[1]%2==0:
            even.append(i)
        else:
            odd.append(i)
    if len(even)>len(odd):
        return(odd[0][0])
    else:
        return(even[0][0])
