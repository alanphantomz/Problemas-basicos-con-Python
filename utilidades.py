def leeLista(n,array,msj):
    print(msj)
    for  i in range(n):
        array.append(int(input(str(i)+": ")))

def muestraLista(array,msj):
    print(msj)
    for i in array:
        print(i,"",end="")
