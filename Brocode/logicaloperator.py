#logicaloperator=checks to see two or more conditions are true

test1= int(input("enter your score in test1 : "))
test2= int(input("enter your score in test2 : "))

if test1 > 17 and test2 >17:
    print("you did good in both test!")
elif test1 > 17 or test2 > 17:
    print("you did good in one test!")
elif test1<10 and test2<10:
    print("you piece of shit!")        
