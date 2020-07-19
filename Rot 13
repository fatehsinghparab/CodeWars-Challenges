def rot13(message):
    string = []
    upper_letter,lower_letter  = list(range(65,91)),list(range(97,123))
    for i in message:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122:
            if (i.isupper()==True):
                count = 0
                for j in (upper_letter[upper_letter.index(ord(i)):]+upper_letter[:upper_letter.index(ord(i))]):      
                    if count == 13:
                        string.append(chr(j))
                    count += 1
            else:
                count = 0
                for j in ( lower_letter[ lower_letter.index(ord(i)) : ] + lower_letter[:lower_letter.index(ord(i))] ):
                    if count == 13:
                        string.append(chr(j))
                    count += 1
        else:
            string.append(i)
    return "".join(string)
