# input() is used to take an input from a user.
# generally input() takes the input as string datatype, but we change it by typecasting.
# if we need to use the input, we should store it in some variable

name = input("what is your name? : ")
print("hi"+" "+name)
age= int(input("what is your age? i will add 10 to it : "))
age=age+10
print("you age now is "+ str(age))
height= float(input("what is your height? : "))
print("your height is " + str(height)+"cm")