print("Calcular el valor de la siguiente sumatoria s=0/1+1/2+1/4+2/7+3/11+5/16+...")
sumTotal=0
fibo,a,b=1,-1,1
adiv=0
div=1
n=int(input("n:"))
while n > 0:
    fibo=a+b
    a,b=b,fibo
    div=div+adiv
    adiv+=1
    sumTotal=sumTotal+fibo/div
    n-=1
print("La sumatoria es %f"%sumTotal)
    
