
y=[]
z=[]

numy_str=input()
numy1,numy2=map(int,numy_str.split())
y.append(numy1)
y.append(numy2)
numz_str=input()
numz1,numz2=map(int,numz_str.split())
z.append(numz1)
z.append(numz2)
    
res=y[0]*z[0]
res1=y[1]+z[1]

print(res+res1)    

    

