print("Generar la siguiente serie 2 1 3 5 3 5 7 7 11 13 17 19 9 11 13 15 17 19 21 23 23 29 31 37 41")
n=int(input("n:"))
a,b,fibo,sw,sw2,k,imp,p,t=1,0,1,0,0,1,1,2,2
while(n>0):
    if sw == 0 :
        fibo=a+b
        a=b;b=fibo;sw=1
    elif sw2==0:
        while n>0 and k<=fibo:
            if p%t==0:
                if p==t:
                    print(p,"",end="")
                    n-=1;k+=1
                p+=1;t=2
            else: t+=1
        sw2=1;k=1;sw=0
    else:
        while n>0 and k<=fibo:
            print(imp,"",end="")
            imp+=2;n-=1;k+=1
        sw2=0;k=1;sw=0
            
                    
