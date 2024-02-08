#tuples= same as list, but this time, tuples are ordered and they are unchangable.

student=("akhil",18,"male")
print(type(student))
print(student.count("akhil"))
print(student.index("male"))

for x in student:
    print(x)

if "yeddu" in student:
    print("yeddu is present!")
else:
    print("yeddu is not here!")        