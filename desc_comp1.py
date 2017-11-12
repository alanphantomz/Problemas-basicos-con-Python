print("Pedir un numero entero positivo e indicar cuantos digitos tiene")
n=int(input("n:"))
nDig=0
while(n>0):
    n=n//10
    nDig+=1
print("Numero de digitos: %d"%nDig)

