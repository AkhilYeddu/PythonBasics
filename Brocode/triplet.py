
y=[]

num_str=input()
num1,num2,num3=map(int,num_str.split())
    
y.append(num1)
y.append(num2)
y.append(num3)
y.sort()
print(y[1])


       