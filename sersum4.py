print("Generar la siguiete serie: 1,2,2,3,3,3,4,4,4,4,5,...")
n=int(input("n:"))
incrementa=1
contador=1
while n>0:
    if(contador<=incrementa):
        print("%d, "%incrementa,end="")
        contador+=1
        n-=1
    else:
        contador=1
        incrementa+=1
    
    
