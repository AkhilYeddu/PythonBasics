import os
text="i just removed the older text, but doesnt go because of append\ngreat!"
with open("write.txt","a") as file: # default is read, if we mention ,"W" we can write
    file.write(text)
# "a" does append, if we use "w" to write something, the previous one gets overwritten, so use append    