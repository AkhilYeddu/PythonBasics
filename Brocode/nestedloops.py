#nested loops= the "inner loop" will finish all of its iterations before finishing one iteration of the outer loop.
rows= int(input("how many rows? : "))
columns= int(input("how many columns? : "))
symbol= input("enter the symbol you want to use : ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()    