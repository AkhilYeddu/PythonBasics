#*args= paramter that will pack all the arguements in a tuple
# useful so that a function can a accept a  varrying amount of positional arguements.

def add(*args):
    sum=0 
    for i in (args):
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,9,10))    