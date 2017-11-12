def datosPersona(nacimiento,nom,apPat,apMat):
    edad=2017-nacimiento
    nombreCompleto=nom+" "+apPat+" "+apMat
    apellidos=apPat+" "+apMat
    return (edad,nombreCompleto,apellidos)

def main():
    (a,b,c)=datosPersona(1993,"Alan","Quispe","Velasquez")
    print("Edad: %d\nNombre completo: %s\nApellidos: %s"%(a,b,c))

main()