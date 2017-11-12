#modulo de numeros fibonacci
def fib(n):#escribe la serie fibo hasta n
    a,b = 0,1
    while b<n:
        print(b,end=' ')
        a,b=b,a+b
    print()

def fib2(n):#devuelve la serie fibo hasta n
    res=[]
    a,b=0,1
    while b < n:
        res.append(b)
        a,b=b,a+b
    return res
