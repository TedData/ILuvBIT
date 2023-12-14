def hti(xs,v,h): 
    i=h 
    inc=0 
    n=len(xs) 
    while xs[i] is not None: 
        if xs[i]==v: 
            return 
        inc +=1 
        i=(i+inc)%n 
    xs[i]=v 

xs=[4,None,5,6,None,7,8]
hti(xs,6,6)
print(xs)
