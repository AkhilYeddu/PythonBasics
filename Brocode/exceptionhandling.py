#Exception Handling = events detected during excution that interrupt the normal workflow of a program.
#handling these type of events and ensuring the normal workflow is called exception handling

try:
    numerator=int(input("Enter numerator: "))
    denominator=int(input("Enter denominator: "))
    result=numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by 0 !")
except ValueError as e:
    print(e)
    print("enter numbers only")
except Exception as e:
    print(e)
    print("something went wrong")

else:
    print(result)
finally:
    print("this is written in finally block, it will always execute")        

