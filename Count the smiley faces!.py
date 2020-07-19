def count_smileys(arr):
    content = [ (":",";"),("-","~"," "),(")","D")]
    count = 0
    for smiley in arr:
        print(smiley)
        chk = 0
        
        if len(smiley)<3:
            smiley = [element for element in smiley]
            smiley.insert(1," ")
        print(smiley,"\n")
        for i in range(3):
            if smiley[i] in content[i]:
                chk +=1
            else:
                chk -= 1
        if chk >1<=3:
            count +=1
        print(chk,"\n")
    print(count,"\n")
    return count
