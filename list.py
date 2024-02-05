food=["pizza","burger","fried chicken","noodles","biryani","fried rice"]

print(food[3])
print("")

food[3]="cake"
food.append("sushi")
food.pop() #removes last element
food.insert(0,"pasta")
food.remove("fried rice")
food.sort() #sorts in alphabetical order
food.clear()
for i in food:
    print(i)

