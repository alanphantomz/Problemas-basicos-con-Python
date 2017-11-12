def ordena(lista):
    """Ordena la lista de nombres recibida alfabeticamente"""
    for i in range(len(lista)):
        masPeq=lista[i]
        pos=i
        for j in range(i+1,len(lista)):
            if masPeq > lista[j]:
                masPeq=lista[j]
                pos=j
        aux=lista[i]
        lista[i]=lista[pos]
        lista[pos]=aux

def muestra(lista):
    for k in range(len(lista)):
        print("[%s]"%lista[k],end="")

def llena(n):
    lista = []
    for i in range(n):
        lista.append(input("[%d]:" %(i+1)))
    return lista


#Comienzo del programa
ejercicio="""Dado un vector de cadenas ordenar
alfabéticamente sus elementos."""
print(ejercicio)

n = int(input("Ingrese n:"))
lista=llena(n)

ordena(lista)

print("La lista ordenada es:")
muestra(lista)