print("Generar la siguiente serie: 1 0 0 1 1 1 0 0 0 0 1 1 1 1 1...")
n=int(input("n:"))
sw=1
limite=1
k=1
while n>0:    
    if k<=limite:
        print("%d "%sw,end="")
        k+=1
    else:
        sw=1-sw
        limite+=1
        k=1
    
    n-=1
