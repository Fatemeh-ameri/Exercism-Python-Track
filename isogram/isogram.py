def is_isogram(string):
    if string == "":
        return True
    string = string.lower()
    string = string.replace("-","")
    string = string.replace(" ","")
    temp = []
    for i in string:
         temp.append(string.count(i))
    if sum(temp) == len(string):
        return True
    else:
        return False    
           
