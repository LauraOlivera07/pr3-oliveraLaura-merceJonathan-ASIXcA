"""
Laura Olivera - Jonathan Merce
4/12/2023
ASIXcA M03 UF1 A4

Programa que demana a l'usuari la introducció de 10 nombres sencers
(que també podrien ser 10000000 😱😳😈) i ha de mostrar,
al final i per pantalla, quants són positius, quants negatius i quants zero.
"""
contadorpositiu= 0
contadornegatiu=0
zero= 0

try:
    for i in range(1, 11): #per cada iteració de l'1 al 10 demanarà un número
        numero=int(input(f"{i}. Introdueix un nombre: "))

        if numero<0:
            contadornegatiu +=1 #si el número és inferior a 0, sumarà 1 al comptador de nombres negatius
        elif numero>0:
            contadorpositiu +=1 #si el número és superior a 0, sumarà 1 al comptador de nombres positus
        else:
            zero +=1 #si no es dona cap situació anterior, sumarà 1 al comptador de zeros

    print(f"Has introduït {contadorpositiu} números positius, {contadornegatiu} números negatius i {zero} zeros.")

except ValueError:
    print("Has d'introduïr un número sencer.")


