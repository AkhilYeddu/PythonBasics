#scope=the region where is identifier is defined
#both local and global scope can exist at the same time.
name="yeddu" # this is a global scope, it is recognisable both inside and outside the function.
def display_name():
    name="akhil" #here name is a local scope, it is only recognisable inside the function
    print(name)

print(name)
display_name()
    
