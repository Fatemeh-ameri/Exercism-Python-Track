# has 3 as a factor, add 'Pling' to the result.
# has 5 as a factor, add 'Plang' to the result.
# has 7 as a factor, add 'Plong' to the result.
# does not_ have any of 3, 5, or 7 as a factor, the result should be the digits of the number.
def convert(number):
    if(number % 3 == 0 and number % 5 == 0 and number % 7 == 0):
        return("PlingPlangPlong")
    elif(number % 3 == 0 and number % 5 == 0):
        return("PlingPlang")
    elif(number % 3 == 0 and number % 7 == 0):
        return("PlingPlong")
    elif(number % 5 == 0 and number % 7 == 0):
        return("PlangPlong")
    elif(number % 3 == 0):
        return("Pling")
    elif(number % 5 == 0):
        return("Plang")
    elif(number % 7 == 0):
        return("Plong")
    else:
        return(str(number))
