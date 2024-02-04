#if statements= a block of code that executes only if statement is true
# order matters in  if statements.

age=int(input("how old are you?: "))

if age>100:
    print("you should be dead by now!")
elif age >=18:
    print("you are an adult!")
elif age<0:
    print("you havent been born yet!")    
else:
    print("you are a child!")    