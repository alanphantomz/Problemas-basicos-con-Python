"""Escrito by: Alan"""
from algoritmos_basicos.modulo_vec import llenarLista
from algoritmos_basicos.modulo_vec import mostrarLista
ejercicio="Hacer leer un vector v de n elementos y hallar" \
          "el promedio general y el promedio de los numeros" \
          "pares e impares"

print(ejercicio)
n=int(input("Ingrese n: "))
lista=llenarLista(n,"Engrese los elementos uno a uno:")
mostrarLista(lista,"He aqui los elementos ingresados")
promGeneral=0
promImpares=0
promPares=0
cpi=0
cpp=0
for i in lista:
    promGeneral+=i
    if i%2==0:
        promPares+=i
        cpp+=1
    else:
        promImpares+=i
        cpi+=1
promGeneral/=len(lista)
promImpares/=cpi
promPares/=cpp
print("\nPromedio General = %f"%promGeneral)
print("Promedio Impares = %f"%promImpares)
print("Promedio Pares = %f"%promPares,end="")