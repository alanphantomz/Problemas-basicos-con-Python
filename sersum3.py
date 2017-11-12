print("Generar la siguiente serie 2 1 3 5 3 5 7 7 11 13 17 19 9 11 13 15 17 19 21 23 23 29 31 37 41")
print("Mezcla de primos, fibos e impares")
n=int(input("n:"))
esPrimo=2
inpar=1
fibo=1
a=0
b=1
cFibo=1
swInpPrim=1
while n>0:    
    if cFibo<=fibo:
        if swInpPrim==1:
            i=1
            nDivs=0
            while i<=esPrimo:
                if (esPrimo%i)==0:
                    nDivs+=1
                i+=1
            if nDivs==2:
                print("%d "%esPrimo,end="")
                n-=1
                cFibo+=1
            esPrimo+=1
        else:
            print("%d "%inpar,end="")
            n-=1
            inpar+=2
            cFibo+=1
    else:
        fibo = a+b
        a=b
        b=fibo
        cFibo=1
        swInpPrim=1-swInpPrim
 
