import string


def abbreviate(words):
    words = words.replace("-"," ").replace("_"," ").split()
    empty_string = ""
    for i in words:
        empty_string  += i[0][0].upper()
    return empty_string

   

