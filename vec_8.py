"""Muy interesante"""
from algoritmos_basicos.modulo_vec import llenarLista
from algoritmos_basicos.modulo_vec import mostrarLista

def isCapicua(num):
    nNum=""
    for i in str(num):
        nNum=i+nNum
    if str(num)==nNum:return True
    else: return False

ejercicio="Hacer leer un vector v de n elementos con numeros\n" \
          "mayores a 100, determinar cuantos numeros capicuas \n" \
          "hay en el vector, desplegar contador de capicuas"
print(ejercicio)
n=int(input("n: "))
lista=llenarLista(n,"Ingrese por favor un mensaje")
mostrarLista(lista,"Elementos ingresados")
nCapicuas=0
for i in lista:
    if isCapicua(i):
        nCapicuas+=1
print("Numero de Capicuas: %d"%nCapicuas)