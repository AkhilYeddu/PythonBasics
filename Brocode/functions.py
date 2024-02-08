#functions= a block of code which executes only when it is called.

# 1st WAY
def hello(f_name,l_name): #this is called a parameter, like a nickname to an arguement
    print("hello"+f_name+l_name)
    print("have a nice day!")


hello("Akhil","Yeddu")
hello("Noob","Saibot")    #this is calling the function, and also giving arguements. arguements are the values/data what we sent to function to call so that the compiler can understand

# 2nd WAY
def age(agee):
    print("i know your age!")
    print("you are"+" "+str(agee)+" " +"years old!")


MYage=18

age(MYage)

