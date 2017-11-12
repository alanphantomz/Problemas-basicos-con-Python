"""Write by Alan"""
from algoritmos_basicos.modulo_vec import llenarLista
from algoritmos_basicos.modulo_vec import mostrarLista
ejercicio="Hacer leer un vector v de n elementos, desplegar" \
          "los multiplos de K y las posiciones que ocupan"
print(ejercicio)
n=int(input("n: "))
k=int(input("k: "))
lista=llenarLista(n,"Ingrese los elementos")
mostrarLista(lista,"La lista ingresada es:")
for i in range(len(lista)):
    if lista[i]%k==0:
        print("Elemento: %d, posición: %d"%(lista[i],i+1))

