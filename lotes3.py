ejercicio="""
Pedir un numero entero positivo, después pedir esa cantidad
de números de los cuales se debe mostrar la suma de esos números.
"""
print(ejercicio)
n=int(input("n:"))
sumatoria=0
for i in range(n,0,-1):
    num=int(input("number:"))
    sumatoria=sumatoria+num
print("La suma total es: %d"%sumatoria)

