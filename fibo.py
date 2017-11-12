def fibo(n):#devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de fibonacci hasta n. """
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

print("Ingrese n para la serie de fibonacci: ")
n=int(input(">"))
f11=fibo(n)
print(f11)
