# Given a name, return a string with the message:
# One for name, one for me.
# Where "name" is the given name.
# However, if the name is missing, return the string:
# One for you, one for me.

def two_fer (name = 'you'): 
    return 'One for {0}, one for me.'.format(name)