def llenarLista(n,mensaje=""):
    'Hace llenar una lista de longitud n con mensaje como encabezado'
    lista=[]
    print(mensaje)
    for i in range(n):
        lista.append(int(input("[%d]: "%(i+1))))
    return lista

def mostrarLista(lista,mensaje=""):
    "Se muestra lista con mensaje como encabezado"
    print(mensaje)
    for i in lista:
        print("[%d]"%i,end="")
    print()