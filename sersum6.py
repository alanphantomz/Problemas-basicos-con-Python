print("Dado un numero n, resolver la siguiente serie(con un solo ciclo)\nn=16 la serie:\n0,2,3,1,1,2,5,7,11,13,3,5,8,13,21,17,....")
n=int(input("n:"))
fibo=0
a,b=1,0
primo=2
cDivP=0
divP=1
conSeries=1
incCont=1
swFP=1
while n>0:
    if(incCont<=conSeries):
        if swFP:
            print("%d "%fibo,end="")
            fibo=a+b
            a,b=b,fibo
            n=n-1
            incCont=incCont+1
        else:
            #print primos
            if divP<=primo:
                if primo%divP==0:
                    cDivP+=1
                divP+=1
            else:
                if cDivP==2:
                    print("%d "%primo,end="")                    
                    n-=1
                    incCont=incCont+1
                primo+=1
                divP=1
                cDivP=0
    else:
        conSeries=conSeries+1
        incCont=1
        swFP=1-swFP
