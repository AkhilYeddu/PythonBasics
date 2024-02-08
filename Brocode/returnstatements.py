#return statements= functions in python which are used to return a value or an object.
def multiply(num1,num2):
    return num1*num2
    

x=int(input())
y=int(input())

multiply(x,y)
res=multiply(x,y)
print("multiplication of "+str(x)+" and"+ " "+ str(y)+ " is"+" " + str(res))
