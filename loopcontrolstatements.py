#there are 3.
# break
# continue
# pass

#"While True" is a looping construct in the Python programming language that allows a block of code to be repeated indefinitely.

while True:
    name= input("enter your name : ")
    if name != "":
        break
print("hello!"+name)
phone_number="891-956-2972"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
print()    

for i in range(1,11,1): 
    if i==5:
        continue   
    print(i)

for i in range(1,11): 
    if i==5:
        pass
    else:
        print(i)   
        
