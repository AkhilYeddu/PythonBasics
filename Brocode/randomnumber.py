import random # using the random module

x=random.randint(1,6) #1,6 is the range, ie b/w 1 and 6
y=random.random() #gives random floating numbers
print(x)
print(y)

list=["rock","paper","scissors"]
z=random.choice(list) #chooses random string from the list
print(z)

cards=[1,2,3,4,5,6,7,8,9,"A","Q","K","J"]
random.shuffle(cards)
print(cards)