ejercicio="""
Pedir un numero entero positivo de cualquier cantidad de digitos
e indicar cuantos digitos múltiplos de tres tiene. Por ejemplo
si el numero es 2762153 se muestra 2
"""
print(ejercicio)
number=int(input("number:"))
cMult=0
while(number>0):
    modulo=number%10
    if modulo%3==0:
        cMult+=1
    number=number//10
print("Numero de multiplos: %d"%cMult)
