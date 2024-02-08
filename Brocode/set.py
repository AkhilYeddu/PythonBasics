#a set is like a list, but it is unordered and unindexed. it is faster than a list. And also it doesnt allow any duplicate values.
utensils={"fork","spoon","plate","knife","knife","knife"}
print(type(utensils))
dishes={"plate","cup","glass","knife"}

# utensils.add("whisker")
# utensils.remove("knife")

total=utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

for i in total:
    print(i)
print()
for i in utensils:
    print(i)    