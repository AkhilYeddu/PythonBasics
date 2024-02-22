#str.format()=optional method that gives users more control while displaying the output.

name="Akhil"
place="Vizag"

print("hello im {} and i live in {}".format(name,place)) #{} are placeholders.
print("hello im {1} and i live in {0}".format(name,place)) #positional arguements
print("hello im {name1} and i live in {place2}".format(name1="NoobSaibot",place2="Darkness")) #keyword arguements

food1="pizza"
food2="burger"
text="{1} is better than {0}" #because of the positional arguements, the places changed.
print(text.format(food1,food2))
name="Akhil"
print("Hello my name is {:10}.Nice to meet you".format(name))
print("Hello my name is {:<10}.Nice to meet you".format(name))
print("Hello my name is {0:>10}.Nice to meet you".format(name)) #can use positional arguements.
print("Hello my name is {:^10}.Nice to meet you".format(name))

pi=3.14159
number=100000
print("the value of pi is {:.2f}".format(pi))
print("the number is {:,}".format(number))
print("the number is {:X}".format(number)) #HEXA DECIMAL VALUE
print("the number is {:e}".format(number)) #scientific notation
print("the number is {:b}".format(number)) # binary
print("the number is {:o}".format(number)) #octal
