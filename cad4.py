print("Dada una cadena x contar cuanteas veces aparece la subcadena y")
cadena=input("x:")
subc=input("y:")
cuentaS=0
sup=""
for i in range(len(cadena)-len(subc)+1):
    aux=i
    for j in range(len(subc)):
        sup=sup+cadena[aux]
        aux+=1
    if sup==subc:
        cuentaS+=1
    sup=""
print("El numero de subcadenas es: %d"%cuentaS)
        
    
    
    
