def generate_hashtag(s):
    string = s.split()
    string = [i.title() for i in string]
    string = "#" + "".join(string)
    if len(string)>140 or len(string)==1:
        return False
    else:
        return (string)
