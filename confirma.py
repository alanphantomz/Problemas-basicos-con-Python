def pedir_confirmacion(prompt, reintentos=4, queja='SI o NO por favor!!'):
    while True:
        ok=input(prompt)
        if ok in ('s','S','si','Si','SI'):
            return True
        if ok in ('n','no','No','NO'):
            return False
        reintentos=reintentos-1
        if reintentos<0:
            raise OSError('usuario duro')
        print(queja)

pedir_confirmacion("Realmente desea salir? s/n ",3,"s/n please")
pedir_confirmacion ("¿Sobreescribir? s/n ",queja="s/n please")
