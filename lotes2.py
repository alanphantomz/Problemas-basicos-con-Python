ejercicio="""
Pedir un lote de números hasta que se introduzca un número múltiplo de cinco,
de los cuales se debe indicar cuantos son multiplos de tres, componer en un nuevo número
todos los números de dos digitos positivos, mostrar los resultados. Por ejemplo
si se tiene los numeros 4,12,8,87,125 entonces se muestra 2 multiplos de 3 y 1287 nuevo numero
"""
print(ejercicio)
def nDig(num):
    nd=0
    while num>0:
        num=num//10
        nd+=1
    return nd

cMult=0
nNum=0
num=1
while(num%5!=0):
    num=int(input("number:"))
    if num%3==0:
       cMult+=1
    if nDig(num)==2:
        nNum=nNum*100+num
print("numer de multiplos de 3: %d"%cMult)
print("Nuevo numero: %d"%nNum)
        
