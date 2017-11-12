ejercicio="""Pedir un numero entero de cualquier cantidad de digitos y mostrar en
un nuevo numero los digitos ordenados en forma descendente.
Por ejemplo si el numero es 27821503 se muestra 87532210
"""
print(ejercicio)
number=int(input("number:"))
nNumber=0
for forComp in range(9,-1,-1):
    aux=number
    while(number>0):    
        lastDig=number%10
        if(lastDig==forComp):
            nNumber=nNumber*10+lastDig
        number=number//10
    number=aux
print("Number ordenado: %d"%nNumber)

