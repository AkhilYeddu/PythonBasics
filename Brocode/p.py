x = int(input())


for i in range(x):
    y = int(input())
    last = y % 10

    if y >= 10:
        res = 0
        while y >= 10:
            y = y // 10
            first = y
        res = first + last
        print(res)
    
    elif 1 <= y < 10:
        res=x+y
        print(res)
    

        
        
        


    
    
         



