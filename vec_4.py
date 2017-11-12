def llenaLista(n):
    print("Ingrese uno a uno los elementos del vector:")
    v=[]
    for i in range(n):
        v.append(int(input("v[%d]:"%i)))
    return v

def mostrarLista(lista):
    for i in range(len(lista)):
        print("[%d]"%lista[i],end="")
    return

def elmayor(v):
    may=v[0]
    for i in range(1,len(v)):
        if may<v[i]:
            may=v[i]
    print("\nEl mayor es: %d" %may)
    return

print("Retornar el numero mayor de un vector de numeros")
n=int(input("n:"))
v=llenaLista(n)
print("La lista ingresada: ",end="")
mostrarLista(v)
elmayor(v)
