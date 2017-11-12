
ejercicio="""Pedir un lote de números hasta que se introduzca un número negativo,
de los cuales se debe sumar los pares, multiplicar los impares y
unir en un nuevo número todos los números que sean de un solo digito y positivo,
mostrar los resultados. Por ejemplo si se tiene los sgtes numeros 4,12,5,25,2,-6
entonces se muestra 12 suma de pares, 125 multiplicacion impares y 452 new num.
"""
print(ejercicio)

def nDigit(num):
    cDig=0
    while num>0:
        num=num//10
        cDig+=1
    return cDig

nNum=0
suma=0
prod=1
num=0
while num>=0:
    num=int(input(">>"))
    if nDigit(num)== 1:
        nNum=nNum*10+num
    if num%2==0:
        suma+=num
    else:
        prod*=num
print("Suma de Pares: %d"%suma)
print("Producto de Inpares: %d"%prod)
print("Nuevo number: %d"%nNum)
    
    
